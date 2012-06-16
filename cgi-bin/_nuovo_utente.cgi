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


$CGI::POST_MAX = 1024 * 5000;

my $page = new CGI; 
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
	exit;
}
my $sid = $session->id();

if (!Functions::is_manager($sid)){
  print $page->redirect(-URL=>"gestione_utenti.cgi?error=Creazione utente non permesso - non sei un manager");
	exit;
}

my $role = $page -> param("tipo");

if (!$role || ($role ne "manager" && $role ne "impiegato")) {
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - tipologia utente insensata");
	exit;
}

my $name = $page->param("nome");
if (!$name){
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - nome non inserito");
	exit;
}

my $username = $page->param("username");
if (!$username){
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - username non inserito");
	exit;
}

if(Functions::username_taken($username)){
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - username già in uso");
	exit;
}

my $password = $page->param("password");

if (!$password) {
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - password non inserita");
	exit;
}

my $confirm = $page->param("password2");

if (!$confirm) {
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - conferma password non inserita");
	exit;
}

if (!($password eq $confirm)) {
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - la password e la conferma non erano uguali");
	exit;
}

if (length($password) < 6) {
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - la password deve essere di almeno 6 caratteri");
	exit;
}


$password = Functions::crypt_password($password);

my $gender = $page -> param("sesso");

if (!$gender || ($gender ne "M" && $gender ne "F")) {
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - sesso insensato");
	exit;
}

my $age = $page -> param("eta");
my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$age =~ s/$find/$replace/g;


my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$age =~ s/$find/$replace/g;

if (!isint($age)){ # bisogna fare il controllo o con una regexp o con scalar::utils
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - età insensata");
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


$new_worker->appendChild($username_element);
$new_worker->appendChild($password_element);
$new_worker->appendChild($name_element);
$new_worker->appendChild($gender_element);
$new_worker->appendChild($age_element);


$root->appendChild($new_worker);

my $xmlschema = XML::LibXML::Schema->new( location => "../xml/worker.xsd" );
if (!eval { $xmlschema->validate( $doc ); }) {
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - validazione xml non riuscita");
	exit;
}

open(XML,'>../xml/workers.xml') || file_error();
print XML $root->toString();
close(XML);

print $page->redirect("gestione_utenti.cgi");


exit;


sub file_error{
	print $page->redirect(-URL=>"nuovo_utente.cgi?error=Creazione utente non riuscita - errore nella scrittura del file: $!");
	exit;
}








