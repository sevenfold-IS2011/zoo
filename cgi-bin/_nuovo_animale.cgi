#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use File::Basename;
use Functions;
use strict;
use warnings;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;
use Scalar::Util::Numeric qw(isnum isint isfloat);

$CGI::POST_MAX = 1024 * 5000;


my $page = new CGI; 
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
	exit;
}
my $sid = $session->id();


my $area = $page->param("area");
if(!Functions::area_exists($area)){
	print $page->redirect(-URL=>"nuovo_animale.cgi?error=Creazione animale fallita - l'area specificata non esiste");
	exit;
}
my $animal_name = $page->param("nome");
if(Functions::animal_name_taken($animal_name)){
	print $page->redirect(-URL=>"nuovo_animale.cgi?error=Creazione animale fallita - esiste già un animale con questo nome");
	exit;
}
my $gender = $page->param("sesso");
if($gender != "Female" && $gender !="Male"){
	print $page->redirect(-URL=>"nuovo_animale.cgi?error=Creazione animale fallita - sesso insensato");
	exit;
}

my $age = $page->param("eta");
my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$age =~ s/$find/$replace/g;

if (!isint($age)){ # bisogna fare il controllo o con una regexp o con scalar::utils
	print $page->redirect(-URL=>"nuovo_animale.cgi?error=Creazione animale fallita - sesso insensato");
	exit;
}

my $filename = $page->param("image"); 
if (!$filename){ 
	print $page->redirect(-URL=>"nuovo_animale.cgi?error=Caricamento immagine fallito, prova un'immagine più piccola");
	exit;
	}

my $upload_dir = "../public_html/images/animals";
my $upload_path = "../images/animals";

my ($name, $path, $extension) = fileparse($filename, '\..*');
$filename = $name.$extension;

#manca un check sull'image name, occhio

my $upload_filehandle = $page->upload("image");


my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/animals.xml");
my $root = $doc->getDocumentElement();

my $new_animal = $doc->createElement("animale");

my $name_element = $doc->createElement("nome");
$name_element->appendTextNode($animal_name);

my $gender_element = $doc->createElement("sesso");
$gender_element->appendTextNode($gender);

my $img_element = $doc->createElement("img");
my $img_path = $upload_path.'/'.$filename;
$img_element->appendTextNode($img_path);

my $age_element = $doc->createElement("eta");
$age_element->appendTextNode($age);

$new_animal->appendChild($name_element);
$new_animal->appendChild($gender_element);
$new_animal->appendChild($age_element);
$new_animal->appendChild($img_element);

my $xpc = XML::LibXML::XPathContext->new;
$xpc->registerNs('zoo', 'http://www.zoo.com');


my $area_element = $xpc -> findnodes("//zoo:area[\@id=$area]", $doc)->get_node(1); #xpath parte da 1 
$area_element->appendChild($new_animal);

my $doc2 = $parser->parse_string($root->toString());
my $xmlschema = XML::LibXML::Schema->new( location => "../xml/animal.xsd" );
if (eval { $xmlschema->validate( $doc2 ); } eq undef) {
	print $page->redirect(-URL=>"nuovo_animale.cgi?error=Creazione animale non riuscita - validazione xml non riuscita");
	exit;
}

open(XML,'>../xml/animals.xml') || file_error();
print XML $root->toString();
close(XML);

open (UPLOADFILE, ">$upload_dir/$filename" ) || file_error();
binmode UPLOADFILE; 
while (<$upload_filehandle>){ 
	print UPLOADFILE;
	 }
close UPLOADFILE;



print $page->redirect( -URL => "gestione_animali.cgi");

exit;

sub file_error{
	print $page->redirect(-URL=>"nuovo_animale.cgi?error=Creazione animale fallita - errore nella scrittura del file: $!");
	exit;
}

