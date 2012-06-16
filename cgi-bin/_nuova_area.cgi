#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use warnings;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;
use Scalar::Util::Numeric qw(isnum isint isfloat);


my $page = new CGI;
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
	exit;
}
my $sid = $session->id();

my $area_name = $page->param("nome");
if (!$area_name) {
	print $page->redirect(-URL=>"nuova_area.cgi?error=Creazione area fallita - non hai inserito il nome");
	exit;
}

my $area_pos = $page->param("posizione");
if (!$area_pos) {
	print $page->redirect(-URL=>"nuova_area.cgi?error=Creazione area fallita - non hai inserito la posizione");
	exit;
}

my $area_food = $page->param("cibo");

my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$area_food =~ s/$find/$replace/g;

if (!isfloat($area_food) && !isint($area_food)){ 
	print $page->redirect(-URL=>"nuova_area.cgi?error=Creazione area fallita - la quantità di cibo non è un valore valido");
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

my $doc2 = $parser->parse_string($root->toString());
my $xmlschema = XML::LibXML::Schema->new( location => "../xml/animal.xsd" );
if ($xmlschema->validate( $doc2 )) {
	print $page->redirect(-URL=>"nuova_area.cgi?error=Creazione area non riuscita - validazione xml fallita");
	exit;
}

open(XML,'>../xml/animals.xml') || file_error();
print XML $root->toString();
close(XML);	
print $page->redirect( -URL => "gestione_area.cgi");
  
exit;


sub file_error{
	print $page->redirect(-URL=>"nuova_area.cgi?error=Creazione area fallita - errore nella scrittura del file: $!");
	exit;
}
