#!/usr/bin/perl
use CGI;
use CGI::Session;
use File::Spec;

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
my @pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	 $value =~ tr/+/ /;
	 $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/g; 
	 $name =~ tr/+/ /;
	 $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/g; 
	$input{$name} = $value;
}







$page = new CGI;

if ($input{"username"} eq "ciao" && $input{"password"} eq "ciao"){
	$session = new CGI::Session("driver:File", undef, {File::Spec->tmpdir});
	$session->param("name", "Carcarlo Pravettoni");
	
	$cookie = $page->cookie(CGISESSID => $session->id);
	print $page->header( -cookie=>$cookie );
	
	
}else{
	print $page->redirect( -URL => "animali.cgi");
}


exit;
