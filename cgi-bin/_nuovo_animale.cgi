#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;


$CGI::POST_MAX = 1024 * 5000;
my $upload_dir = "/images/animals";

my $page = new CGI; 
my $filename = $page->param("image"); 
if (!$filename){ 
	print $page->header();
	print "There was a problem uploading your photo (try a smaller file). Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
	}
my $area = $page->param("area");
if(!Functions::area_exists($area)){
	print $page->header();
	print "Area non esistente. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}
my $name = $page->param("nome");
if(Functions::name_in_area_taken($area, $name)){
	print $page->header();
	print "Nome già presoin quell'area. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}
my $gender = $page->param("sesso");
if($gender != "Female" && $gender !="Male"){
	print $page->header();
	print "Gender insensato. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}

my $age = $page->param("eta");
my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$age =~ s/$find/$replace/g;

if ($age < 0 || $age > 150){ # bisogna fare il controllo o con una regexp o con scalar::utils
	print $page->header();
	print "age insensato. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}

my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/animals.xml");
my $root = $doc->getDocumentElement();

my $new_animal = $doc->createElement("animale");

my $name_element = $doc->createElement("nome");
$name_element->appendTextNode($name);

my $gender_element = $doc->createElement("sesso");
$gender_element->appendTextNode($gender);

my $age_element = $doc->createElement("eta");
$age_element->appendTextNode($age);
#manca l'immagine
$new_animal->appendChild($name_element);
$new_animal->appendChild($gender_element);
$new_animal->appendChild($age_element);

my $area_element = $root -> findnodes("area[\@id=$area]")->get_node(1); #xpath parte da 1 
#$area_element->appendChild($new_animal);
##print $root->toString(1);
#open(XML,'>../xml/animals.xml') || die("Cannot Open file $!");
#print XML $root->toString();
#close(XML);



print $page->header();
print "Area $area, nome $name, genere $gender e età $age - ";
#print $area_element->toString();
print $root -> findnodes("/")->size();
#print $new_animal -> toString();

exit;

