#!/usr/bin/perl

use CGI;
use CGI::Session;
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
#TO DO: tutti i controlli sui parametri
my $nome_cibo = $page->param("nome");
my $quantita_cibo = $page->param("quantita");
my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/warehouse.xml");
my $root = $doc->getDocumentElement();
my $xpc = XML::LibXML::XPathContext->new;
$xpc->registerNs('zoo', 'http://www.zoo.com');
my $new_cibo = $doc->createElement("cibo");
#$new_cibo->setAttribute("id",$cibo_id);
$new_cibo->setAttribute("nome",$nome_cibo);
$new_cibo->setAttribute("quantita",$quantita_cibo);
$root->appendChild($new_cibo);
open(XML,'>../xml/warehouse.xml') || die("Cannot Open file $!");
print XML $root->toString();
close(XML);

print $page->redirect( -URL => "gestione_magazzino.cgi");
exit;

