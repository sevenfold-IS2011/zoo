#!/usr/bin/perl

package Functions;

use File::Spec;
use CGI::Session;
use XML::XPath;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
#use HTML::Tidy;
use strict;


sub get_name_from_sid{
	my $session = new CGI::Session(undef, $_[0], {File::Spec->tmpdir});
  return $session->param("name");
}

sub get_username_from_sid{
	my $session = new CGI::Session(undef, $_[0], {File::Spec->tmpdir});
  return $session->param("username");
}

sub edit_animal{
	my $name = $_[0];
	print '';
}


sub check_credentials{
	my $username = $_[0];
	my $pswd = $_[1];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	my $nodeset = $xp->find("//impiegato[username=\"$username\"]/password | //manager[username=\"$username\"]/password");
	my @password;
	my $password;
	my $salt = "zxcluywe6r78w6rusdgfbkejwqytri8esyr mhgdku5u65i75687tdluytosreasky6";
	if (my @nodelist = $nodeset->get_nodelist) {
		@password = map($_->string_value, @nodelist);
		$password=@password[0];
	}
	if (crypt($pswd,$salt) eq $password){
		return 1;
	}else{
		return undef;
	}
}

sub crypt_password{
	my $password = $_[0];
	my $salt = "zxcluywe6r78w6rusdgfbkejwqytri8esyr mhgdku5u65i75687tdluytosreasky6";
	return crypt($password, $salt);
}

sub get_employee_name{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	my $nodeset = $xp->find("//impiegato[username=\"$username\"]/nome | //manager[username=\"$username\"]/nome");
	my @name;
	my $name;
	if (my @nodelist = $nodeset->get_nodelist) {
		@name = map($_->string_value, @nodelist);
		$name=@name[0];
	}
	return $name;
}

sub is_manager{
	my $username = get_username_from_sid($_[0]);
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	my $nodeset = $xp->find("//manager[username=\"$username\"]/nome");
	if ($nodeset->size() > 0) {
		return 1;
	}else{
		return undef;
	}

}


sub get_areas{
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find('//@nome | //@id');
	my @stuff;
	my $node;
	if (my @nodelist = $nodeset->get_nodelist) {
		my $j = 0;
		foreach $node (@nodelist){
			@stuff[$j]=$node->getData;
			#print $node->getData;
			#print $j;
			$j = $j + 1;
		}
	}
	return @stuff;

}

sub max_area_id{
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find('//@id');
	if (my @nodelist = $nodeset->get_nodelist) {
		my $max_id = 0;
		my $j = 0;
		my $id;
		foreach $id (@nodelist){
			if ($id->getData() > $max_id){
				$max_id = $id->getData();
			}
		}
		return $max_id + 1;
	} else {
		return 1;
	}
}

sub area_exists{
	my $areaid = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find("//area[\@id=$areaid]");
	if ($nodeset->size > 0){
		return 1;
	} else {
		return undef;
	}
}

sub name_in_area_taken{
	my $areaid = $_[0];
	my $name = $_[1];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find("//area[\@id=$areaid]//animale[nome=\"$name\"]");
	if ($nodeset->size > 0){
		return 1;
	} else {
		return undef;
	}
}

sub animal_table{
	my $source = XML::LibXML->load_xml(location => '../xml/animals.xml');
	my $xslt = XML::LibXSLT->new();
	my $style_doc;
	if ($_[0] == "true"){
	  $style_doc = XML::LibXML->load_xml(location=>"../xml/animals_table_template.xsl", no_cdata=>1);
	}
	else{
	  $style_doc = XML::LibXML->load_xml(location=>"../xml/animals_table_noscript_template.xsl", no_cdata=>1);
	}
	my $stylesheet = $xslt->parse_stylesheet($style_doc);
	my $results = $stylesheet->transform($source);
	my $text = $stylesheet->output_as_bytes($results);
	my $find = '<?xml version="1.0"?>';
	my $replace = "";
	$find = quotemeta $find; # escape regex metachars if present
	$text =~ s/$find/$replace/g;
	return $text;
}

sub users_table{
	my $source = XML::LibXML->load_xml(location => '../xml/workers.xml');
	my $xslt = XML::LibXSLT->new();
 	my $sid = $_[0];
 	my $style_doc;
 	if (Functions::is_manager($sid)){
		$style_doc = XML::LibXML->load_xml(location=>"../xml/workers_table_template_manager.xsl", no_cdata=>1);
	}
	else{
		$style_doc = XML::LibXML->load_xml(location=>"../xml/workers_table_template.xsl", no_cdata=>1);
	}
	my $stylesheet = $xslt->parse_stylesheet($style_doc);
	my $results = $stylesheet->transform($source);
	my $text = $stylesheet->output_as_bytes($results);
	my $find = '<?xml version="1.0"?>';
	my $replace = "";
	$find = quotemeta $find; # escape regex metachars if present
	$text =~ s/$find/$replace/g;
	return $text;
}

sub warehouse_table(){
	my $source = XML::LibXML->load_xml(location => '../xml/warehouse.xml');
	my $xslt = XML::LibXSLT->new();
	my $style_doc = XML::LibXML->load_xml(location=>"../xml/warehouse_table_template.xsl", no_cdata=>1);
	my $stylesheet = $xslt->parse_stylesheet($style_doc);
	my $results = $stylesheet->transform($source);
	my $text = $stylesheet->output_as_bytes($results);
	my $find = '<?xml version="1.0"?>';
	my $replace = "";
	$find = quotemeta $find; # escape regex metachars if present
	$text =~ s/$find/$replace/g;

#sostituisco nella tabella gli id con il nome delle aree
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $idlist = $xp->find('//@id');
	if (my @idarray = $idlist->get_nodelist) {
		my $node;
		my $tmp;
		foreach $tmp (@idarray){
			$node = $tmp->getData;
			my $namelist = $xp->find("//area[\@id=\"$node\"]/\@nome");
			if (my @namearray = $namelist->get_nodelist){
				my $nome;
				$nome = @namearray[0]->getData;
				my $find = "<a href=\"area.cgi?id=$node\">$node</a>";
				my $replace = "<a href=\"area.cgi?id=$node\">$nome</a>";
				$find = quotemeta $find; # escape regex metachars if present
				$text =~ s/$find/$replace/g;
			}
		}
	}
	return $text;
}

sub area_table(){
	my $source = XML::LibXML->load_xml(location => '../xml/animals.xml');
	my $xslt = XML::LibXSLT->new();
	my $style_doc = XML::LibXML->load_xml(location=>"../xml/area_table_template.xsl", no_cdata=>1);
	my $stylesheet = $xslt->parse_stylesheet($style_doc);
	my $results = $stylesheet->transform($source);
	my $text = $stylesheet->output_as_bytes($results);
	my $find = '<?xml version="1.0"?>';
	my $replace = "";
	$find = quotemeta $find; # escape regex metachars if present
	$text =~ s/$find/$replace/g;
	return $text;
}

sub username_taken{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	my $idlist = $xp->find('//');
	
#	my $nodeset = $xp->find("//username=\"$username\"");
	if ($xp->find("//username=\"$username\"")){
		return 1;
	} else {
		return undef;
	}
}

sub get_animal_gender{
	my $animal_name = $_[0];
	my $area = $_[1];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	return $xp->find("//area[\@id=$area]/animale[nome=\"$animal_name\"]\sesso")->string_value();
	
}

#sub orderXML{
#        my $hashParameters = shift;
#        my $encoding = $hashParameters->{encoding};
#        if (!defined($encoding)){
#                $encoding = "raw";
#        }
#
#        # use HTML::Tidy to order the HTML generated!
#        my $tidy = HTML::Tidy->new({
#                'indent'          => 1,
#                'break-before-br' => 1,
#                'output-xhtml'    => 1,
#                'char-encoding'   => $encoding,
#                'doctype'         => 'strict',
#        });

#        my $htmlText = $hashParameters->{htmlText};

        # decode the output to utf-8 so it works correctly
 #       $htmlText = decode("utf-8", $htmlText);
        # clean the HTML
  #      $htmlText = $tidy->clean($htmlText);
        # encode it in utf-8 as used in the html pages
   #     $htmlText = encode("utf-8", $htmlText);
        # delete the generator produced by HTML Tidy. It's simply useless. Here it's an example:
        #<meta name="generator" content="HTML Tidy for Linux/x86 (vers 25 March 2009), see www.w3.org" />
    #    $htmlText =~ s/<meta name="generator".*? \/>\n//;
        # the transformation may give this error, an empty (and useless) xmlns attribute, better to delete it
     #   $htmlText =~ s/ ?xmlns="" ?/ /g;
      #  return $htmlText;
#}



1;

