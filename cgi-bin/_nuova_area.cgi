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
my $sid = $page->cookie("CGISESSID") || undef;
if (!$sid){
  print $page->redirect( -URL => "login.cgi");
}else{
  $areaName=$input{"nome"};
  $areaPos=$input{"posizione"};

}