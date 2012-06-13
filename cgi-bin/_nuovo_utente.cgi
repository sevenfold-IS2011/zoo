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
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
	exit;
}
my $sid = $session->id();

if (!Functions::is_manager($sid)){
  print $page->redirect( -URL => "area_privata.cgi");
	exit;
}

my $role = $page -> param("tipo");

if (!$role || ($role ne "manager" && $role ne "impiegato"))) {
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

my $username = $page->param("username");
if (!$username){
	print $page->header();
	print '<h1> Non hai inserito l\'username  (errori da sistemare)</h1>';
	exit;
}

if(Functions::username_taken($username)){
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

if (!$confirm) {
	print $page->header();
	print '<h1> Non hai inserito la conferma della password  (errori da sistemare)</h1>';
	exit;
}

if (!($password eq $confirm)) {
	print $page->header();
	print '<h1> La password e la conferma non corrispondono  (errori da sistemare)</h1>';
	exit;
}

$password = Functions::crypt_password($password);

my $gender = $page -> param("sesso");

if (!$gender || ($gender ne "M" && $gender ne "F")) {
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
$name_element->appendTextNode($name);

my $gender_element = $doc->createElement("sesso");
$gender_element->appendTextNode($gender);

my $age_element = $doc->createElement("eta");
$age_element->appendTextNode($age);

my $salary_element = $doc->createElement("stipendio");
$salary_element->appendTextNode($salary);


$new_worker->appendChild($username_element);
$new_worker->appendChild($password_element);
$new_worker->appendChild($name_element);
$new_worker->appendChild($gender_element);
$new_worker->appendChild($age_element);
$new_worker->appendChild($salary_element);


$root->appendChild($new_worker);
open(XML,'>../xml/workers.xml') || die("Cannot Open file $!");
print XML $root->toString();
close(XML);

print $page->redirect("gestione_utenti.cgi")


exit;









