#!/usr/bin/perl

package functions;

use File::Spec;
use CGI::Session;
use XML::XPath;


sub get_name_from_sid{
	$session = new CGI::Session(undef, $_[0], {File::Spec->tmpdir});
  return $session->param("name");
}


sub check_credentials{
	$username = $_[0];
	$pswd = $_[1];
	
	my $xp = XML::XPath->new(filename=>'xml/workers.xml');
	#//[username="mario"]/password
	my $nodeset = $xp->find("//employee[username=\"$username\"]/password | //manager[username=\"$username\"]/password");
	my @password;
	my $password;
	if (my @nodelist = $nodeset->get_nodelist) {
		@password = map($_->string_value, @nodelist);
		$password=@password[0];
	}
	if ($pswd eq $password){
		return true;
	}else{
		return false;
	}
	
	
	
	
}


1;