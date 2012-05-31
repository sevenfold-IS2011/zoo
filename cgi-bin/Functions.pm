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


sub check_credentials{
	my $username = $_[0];
	my $pswd = $_[1];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	my $nodeset = $xp->find("//employee[username=\"$username\"]/password | //manager[username=\"$username\"]/password");
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

sub get_employee_name{
	my $username = $_[0];
	my $xp = XML::XPath->new(filename=>'../xml/workers.xml');
	my $nodeset = $xp->find("//employee[username=\"$username\"]/name | //manager[username=\"$username\"]/name");
	my @name;
	my $name;
	if (my @nodelist = $nodeset->get_nodelist) {
		@name = map($_->string_value, @nodelist);
		$name=@name[0];
	}
	return $name;
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