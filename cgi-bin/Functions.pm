#!/usr/bin/perl

package Functions;

use File::Spec;
use CGI::Session;
use XML::XPath;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
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
	my $nodeset = $xp->find('//@name | //@id');
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



1;