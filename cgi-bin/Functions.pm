#!/usr/bin/perl

package Functions;

use File::Spec;
use CGI::Session;
use XML::XPath;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;
use warnings;


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

sub get_areaName_from_id{
	my $id = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find("//area[\@id=\"$id\"]/\@nome");
	my $node = $nodeset->get_node(1);
	return $node->getData;
}

sub get_areaPosizione_from_id{
	my $id = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find("//area[\@id=\"$id\"]/\@posizione");
	my $node = $nodeset->get_node(1);
	return $node->getData;
}

sub get_areaCibo_from_id{
	my $id = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find("//area[\@id=\"$id\"]/\@cibo_giornaliero");
	my $node = $nodeset->get_node(1);
	return $node->getData;
}

sub get_ciboNome_from_id{
	my $id = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/warehouse.xml');
	my $nodeset = $xp->find("//cibo[\@id=\"$id\"]/\@nome");
	my $node = $nodeset->get_node(1);
	return $node->getData;
}

# 1-> xml, 2-> xpath, ritorna nodeset
sub run_xpath{
   	my $xp = XML::XPath->new(filename=>$_[0]);
	return $xp->find($_[1]);
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
			$j = $j + 1;
		}
	}
	return @stuff;
}

sub get_areas_checked{
 	my $cibo_id = $_[0];

	my $parser = XML::LibXML->new;
	my $doc = $parser->parse_file("../xml/warehouse.xml");
	my $root = $doc->getDocumentElement();
	my $xpc = XML::LibXML::XPathContext->new;
	$xpc->registerNs('zoo', 'http://www.zoo.com');
	my $xpath_exp = "//zoo:cibo[\@id=\"$cibo_id\"]/zoo:area";
	my $old_aree = $xpc->findnodes($xpath_exp, $doc);	
	my $size = $old_aree->size;
	my @aree;
	for(my $count = 0; $count <= $size ; $count = $count+1){
		my $temp = $old_aree->get_node($count);
		if($temp){
			@aree[$count] = $temp->textContent;
			#print @aree[$count];
		}
	}
	return @aree;
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
sub max_cibo_id{
	my $xp = XML::XPath->new(filename=>'../xml/warehouse.xml');
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

sub animal_name_taken{
	my $areaid = $_[0];
	my $name = $_[1];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $nodeset = $xp->find("//animale[\@nome=\"$name\"]");
	if ($nodeset->size > 0){
		return 1;
	} else {
		return undef;
	}
}

sub cibo_name_taken{
	my $name = $_[0];
	print 'nome: '.$name;
	my $xp = XML::XPath->new(filename=>'../xml/warehouse.xml');
	my $nodeset = $xp->find("//cibo[\@nome=\"$name\"]");
	if ($nodeset->size > 0){
		return 1;
	} else {
		return undef;
	}
}

sub animal_table{
	my $source = XML::LibXML->load_xml(location => '../xml/animals.xml');
	my $xslt = XML::LibXSLT->new();
	my $style_doc = XML::LibXML->load_xml(location=>"../xml/animals_table_template.xsl", no_cdata=>1);
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
	if (Functions::is_manager($_[0])){
		return rendered_template('../xml/workers.xml','../xml/workers_table_template_manager.xsl');
	} else{
		return rendered_template('../xml/workers.xml','../xml/workers_table_template.xsl');
	}
}

sub warehouse_table(){
	my $text = rendered_template('../xml/warehouse.xml',"../xml/warehouse_table_template.xsl");
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
				my $find = "$node\[_\]";
				my $replace = $nome;
				$find = quotemeta $find; # escape regex metachars if present
				$text =~ s/$find/$replace/g;
				my $find = "</a>";
				my $replace = '</a> ';
				$find = quotemeta $find; # escape regex metachars if present
				$text =~ s/$find/$replace/g;
			}
		}
	}
	return $text;
}
# 0->source, 1->template
sub rendered_template{
  my $source = XML::LibXML->load_xml(location => $_[0]);
	my $xslt = XML::LibXSLT->new();
	my $style_doc = XML::LibXML->load_xml(location=>$_[1], no_cdata=>1);
	my $stylesheet = $xslt->parse_stylesheet($style_doc);
	my $results = $stylesheet->transform($source);
	my $text = $stylesheet->output_as_bytes($results);
	my $find = '<?xml version="1.0"?>';
	my $replace = "";
	$find = quotemeta $find; # escape regex metachars if present
	$text =~ s/$find/$replace/g;
	return $text;
}
sub area_table(){
	return rendered_template('../xml/animals.xml','../xml/area_table_template.xsl');
}

sub username_taken{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	
if ($xp->find("//username=\"$username\"")){ #funziona perché torna un booleano
		return 1;
	} else {
		return undef;
	}
}

sub get_animal_gender{
	my $animal_name = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	return $xp->find("//animale[nome=\"$animal_name\"]/sesso")->string_value();
}

sub get_animal_age{
	my $animal_name = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	return $xp->find("//animale[nome=\"$animal_name\"]/eta")->string_value();
}
sub get_animal_img{
	my $animal_name = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	return $xp->find("//animale[nome=\"$animal_name\"]/img")->string_value();
}

sub is_manager_from_username{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	my $size = $xp->find("//manager[username=\"$username\"]")->size();
	if ($size > 0){
		return 1;
	}else{
		return undef;
	}
}

sub get_user_gender{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	return $xp->find("//username[. = \"$username\"]/../sesso")->string_value();
}

sub get_user_name{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	return $xp->find("//username[. = \"$username\"]/../nome")->string_value();
}

sub get_user_age{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	return $xp->find("//username[. = \"$username\"]/../eta")->string_value();
}

sub exhaustion_list{
	my $days = $_[0];
	my $parser = XML::LibXML->new;
	my $doc = $parser->parse_file("../xml/warehouse.xml");
	my $root = $doc->getDocumentElement();
	my $xpc = XML::LibXML::XPathContext->new();
	$xpc->registerNs('zoo', 'http://www.zoo.com');
	my $xpath_exp = "//zoo:cibo";
	my $foods = $xpc -> findnodes($xpath_exp, $doc);
	my $foods_amount = $foods -> size();
	my $food;
	print "<ul>";
	for(;$foods->size() > 0;){
		$food = $foods -> pop();
		#print "exhaustion - controllo ".$food->getAttribute("nome")."<br/>";
		if (!check_availability($food, $days)){
			print "<li> ".$food->getAttribute("nome")."</li>";
		}
	}
	print "</ul>";
}

sub check_availability{
	my $food = $_[0];
	my $availability = $food -> getAttribute("quantita");
	my $days = $_[1];
	if (!$food->hasChildNodes) {
		return undef;
	}
	my $xpc = XML::LibXML::XPathContext->new;
	$xpc->registerNs('zoo', 'http://www.zoo.com');
	my $arealist = $xpc->find('./zoo:area',$food);
	my $daily_use = 0;
	my $area;
	my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
	my $xpath_exp;
	my $areanode;

	for(;$arealist->size > 0;){
		$areanode = $arealist->pop();
	#	print "checkcoso - controllo ".$areanode->toString()." area è una...".$areanode."<br/>";
		$daily_use = $daily_use + daily_area_food($areanode->textContent());
	}
	if ($availability < ($daily_use * $days)){
	#	print "checkcoso: --------------------FINISCE------------<br/>";
		return undef;
	}
	#print "checkcoso: --------------ABBASTANZA--------------<br/>";
	return 1;
}


sub daily_area_food{
	my $area_id = $_[0];
	my $parser = XML::LibXML->new;
	my $doc = $parser->parse_file("../xml/animals.xml");
	my $root = $doc->getDocumentElement();
	my $xpc = XML::LibXML::XPathContext->new();
	$xpc->registerNs('zoo', 'http://www.zoo.com');
	my $xpath_exp = "//zoo:area[\@id=\"$area_id\"]";
	my $area = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
	my $n_animals = $area->childNodes()->size();
	my $animal;
	my $daily_animal_need = $area -> getAttribute("cibo_giornaliero");
#	print "dailycoso: daily_need: $daily_animal_need, n_animals: $n_animals <br/>";	
	return ($daily_animal_need * $n_animals);
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

