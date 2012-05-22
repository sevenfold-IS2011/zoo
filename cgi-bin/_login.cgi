#!/usr/bin/perl
use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
    use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

my $buffer;
my $name;
my $value;
my %input;
my $pair;
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

my $page = new CGI;

if (Functions::check_credentials($input{"username"}, $input{"password"})){
	
	my $session = new CGI::Session("driver:File", undef, {File::Spec->tmpdir});
	$name = Functions::get_employee_name($input{"username"});
	$session->param("name", $name);
	my $cookie = $page->cookie(CGISESSID => $session->id);
	print $page->redirect( -URL => "area_privata.cgi", -cookie=>$cookie);
}else{
	print $page->redirect( -URL => "animali.cgi");
}

exit;
