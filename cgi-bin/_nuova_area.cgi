#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;
use Scalar::Util::Numeric qw(isnum isint isfloat);


my $page = new CGI;
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi");
	exit;
}
my $sid = $session->id();

my $area_name = $page->param("nome");
if (!$area_name) {
	print $page->header();
	print "<h2>Non hai inserito il nome. Questi errori andranno gestiti con un div apposito nella pagina precedente<h2>";
	exit;
}

my $area_pos = $page->param("posizione");
if (!$area_pos) {
	print $page->header();
	print "<h2>Non hai inserito la posizione. Questi errori andranno gestiti con un div apposito nella pagina precedente<h2>";
	exit;
}

my $area_food = $page->param("cibo");

my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$area_food =~ s/$find/$replace/g;

if (!isfloat($area_food)){ 
	print $page->header();
	print "quantità di cibo insensato. Questi errori andranno gestiti con un div apposito nella pagina precedente - $area_food";
	exit;
}

my $area_id = Functions::max_area_id + 1;
my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/animals.xml");
my $root = $doc->getDocumentElement();

my $new_element= $doc->createElement("area");
$new_element->setAttribute("id", $area_id);
$new_element->setAttribute("posizione", $area_pos);
$new_element->setAttribute("nome", $area_name);
$new_element->setAttribute("cibo_giornaliero", $area_food);
$root->appendChild($new_element);

open(XML,'>../xml/animals.xml') || die("Cannot Open file $!");
print XML $root->toString();
close(XML);	
print $page->redirect( -URL => "gestione_area.cgi");
  

exit;