#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;
use Scalar::Util::Numeric qw(isnum isint isfloat);


$CGI::POST_MAX = 1024 * 5000;

my $page = new CGI; 
my $sid = $page->cookie("CGISESSID") || undef;
if (!$sid){
  print $page->redirect( -URL => "login.cgi");
	exit;
}

if (!is_manager($sid)){
  print $page->redirect( -URL => "area_privata.cgi");
	exit;
}

my $role = $page -> param("tipo");

if (!$role || (!($role eq "manager") && !($role eq "impiegato")) {
	print $page->header();
	print '<h1> Ruolo non corretto (errori da sistemare)</h1>';
	exit;
}

my $name = $page->param("nome");
if (!$name){
	print $page->header();
	print '<h1> Non hai inserito il nome  (errori da sistemare)</h1>';
	exit;
}

my $username = $page->param("usernome");
if (!$username){
	print $page->header();
	print '<h1> Non hai inserito l\'username  (errori da sistemare)</h1>';
	exit;
}

if(username_taken($username)){
	print $page->header();
	print '<h1> username già preso (errori da sistemare)</h1>';
	exit;
}

my $password = $page->param("password");

if (!$password) {
	print $page->header();
	print '<h1> Non hai inserito la password  (errori da sistemare)</h1>';
	exit;
}

my $confirm = $page->param("password2");

if (!$password2) {
	print $page->header();
	print '<h1> Non hai inserito la conferma della password  (errori da sistemare)</h1>';
	exit;
}

if (!($password eq $password2)) {
	print $page->header();
	print '<h1> La password e la conferma non corrispondono  (errori da sistemare)</h1>';
	exit;
}

$password = Functions::crypt($password);

my $gender = $page -> param("sesso");

if (!$gender || (!($gender eq "M") && !($gender eq "F"))) {
	print $page->header();
	print '<h1> Sesso non corretto  (errori da sistemare)</h1>';
	exit;
}

my $age = $page -> param("eta");
my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$age =~ s/$find/$replace/g;

if (!isint($age)){ # bisogna fare il controllo o con una regexp o con scalar::utils
	print $page->header();
	print "age insensato. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}

my $salary = $page -> param("stipendio");
my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$age =~ s/$find/$replace/g;

if (!isint($age)){ # bisogna fare il controllo o con una regexp o con scalar::utils
	print $page->header();
	print "Stipendio insensato. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}



my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/workers.xml");
my $root = $doc->getDocumentElement();

my $new_worker = $doc->createElement($role);

my $username_element = $doc->createElement("username");
$username_element->appendTextNode($username);

my $password_element = $doc->createElement("password");
$password_element->appendTextNode($password);

my $name_element = $doc->createElement("nome");
$name_element = $doc->appendTextNode($name);

my $gender_element = $doc->createElement("sesso");
$gender_element = $doc->appendTextNode($gender);

my $age_element = $doc->createElement("eta");
$age_element = $doc->appendTextNode($age);

my $age_element = $doc->createElement("stipendio");
$age_element = $doc->appendTextNode($age);


$new_worker->appendChild($username_element);
$new_worker->appendChild($password_element);
$new_worker->appendChild($nome_element);
$new_worker->appendChild($gender_element);
$new_worker->appendChild($age_element);


#my $xpc = XML::LibXML::XPathContext->new;
#$xpc->registerNs('zoo', 'http://www.zoo.com');


#my $area_element = $xpc -> findnodes("//zoo:./", $doc)->get_node(1); #xpath parte da 1 
$root->appendChild($new_worker);
open(XML,'>../xml/workers.xml') || die("Cannot Open file $!");
print XML $root->toString();
close(XML);













