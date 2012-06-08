#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;

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
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi");
	exit;
}
my $sid = $session->id();
my $areaName = $input{"nome"};
my $areaPos = $input{"posizione"};
my $areaId = Functions::max_area_id + 1;
my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/animals.xml");
my $root = $doc->getDocumentElement();

my $new_element= $doc->createElement("area");
$new_element->setAttribute("id", $areaId);
$new_element->setAttribute("posizione", $areaPos);
$new_element->setAttribute("nome", $areaName);
$root->appendChild($new_element);
	#print $root->toString(1);
open(XML,'>../xml/animals.xml') || die("Cannot Open file $!");
print XML $root->toString();
close(XML);	
print $page->redirect( -URL => "nuova_area.cgi");
  

}






exit;