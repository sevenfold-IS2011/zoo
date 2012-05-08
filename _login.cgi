#!/usr/bin/perl
use CGI::Session;

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

my $logged=0;


if ($input{"username"} eq "ciao" && $input{"password"} eq "ciao"){
	$session = new CGI::Session("driver:File", undef, {Directory=>"/tmp"});
	print $page->redirect( -URL => "index.cgi");
}else{
	print $page->redirect( -URL => "animali.cgi");
}


exit;
