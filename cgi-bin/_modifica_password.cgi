#!/usr/bin/perl

use CGI;
use CGI::Session;
use Functions;
use strict;
use warnings;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;


my $page = new CGI; 

my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
	exit;
}

my $sid = $session->id();
my $old_password = $page -> param("old_password");
my $username = Functions::get_username_from_sid($sid);
if (!Functions::check_credentials($username, $old_password)){
	print $page->redirect( -URL => "modifica_password.cgi?error=Impossibile modificare la password - password errata");
	exit;
}
my $password = $page -> param("password");
if (!$password){
	print $page->redirect( -URL => "modifica_password.cgi?error=Impossibile modificare la password - nuova password non valida");
	exit;
}

if (length($password) < 6){
	print $page->redirect( -URL => "modifica_password.cgi?error=Impossibile modificare la password - la nuova password deve essere di almeno 6 caratteri");
	exit;
}

my $password_confirm = $page -> param("password_confirm");

if (!$password_confirm){
	print $page->redirect( -URL => "modifica_password.cgi?error=Impossibile modificare la password - conferma password non valido");
	exit;
}

if ($password_confirm ne $password) {
	print $page->redirect( -URL => "modifica_password.cgi?error=Impossibile modificare la password - conferma password errata");
	exit;
}

my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/workers.xml");
my $root = $doc->getDocumentElement();
my $xpc = XML::LibXML::XPathContext->new;
$xpc->registerNs('zoo', 'http://www.zoo.com');
my $xpath_exp = "//zoo:username[. = \"$username\"]/../zoo:password";
my $old_password_node = $xpc->findnodes($xpath_exp, $doc)->get_node(1);
my $new_password_node = $doc->createElement("password");
$new_password_node -> appendTextNode(Functions::crypt_password($password));
$old_password_node -> replaceNode($new_password_node);

open(XML,'>../xml/workers.xml') || file_error();
print XML $root->toString();
close(XML);

$session -> delete();

print $page->redirect(-URL=>"login.cgi?error=Password moficata - si prega di rieffettuare il login.");

exit;

sub file_error{
	print $page->redirect(-URL=>"modifica_password.cgi?error=Operazione fallita - errore nella scrittura del file: $!");
	exit;
}



