#!/usr/bin/perl

use CGI;
use CGI::Session;
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
my $nome_cibo = $page->param("nome");#nome non inserito
if(!$nome_cibo){
	print $page->redirect(-URL=>"nuovo_cibo.cgi?error=Inserimento in magazzino non riuscito - nome non specificato");
	exit;
}
if(Functions::cibo_name_taken($nome_cibo)){#nome già presente
	print $page->redirect(-URL=>"nuovo_cibo.cgi?error=Inserimento in magazzino non riuscito - nome già in uso");
	exit;
}
my $quantita_cibo = $page->param("quantita");#quantita non inserito
if(!$quantita_cibo | ( !isint($quantita_cibo) && !isfloat($quantita_cibo) | $quantita_cibo < 0 )){
	print $page->redirect(-URL=>"nuovo_cibo.cgi?error=Inserimento in magazzino non riuscito - quantità insensata");
	exit;
}

my @all_area = Functions::get_areas;
my @area_list;
my $cont = 0;
my $size = scalar @all_area;
for(my $k = 0 ; $k < $size ; $k = $k + 2){
	my $pos = @all_area[$k];
	@area_list[$cont] = $page->param("$pos");
	$cont = $cont +1 ;
}

my $parser = XML::LibXML->new;
my $doc = $parser->parse_file("../xml/warehouse.xml");
my $root = $doc->getDocumentElement();
my $xpc = XML::LibXML::XPathContext->new;
$xpc->registerNs('zoo', 'http://www.zoo.com');
my $new_cibo = $doc->createElement("cibo");
$new_cibo->setAttribute("id",Functions::max_cibo_id);
$new_cibo->setAttribute("nome",$nome_cibo);
$new_cibo->setAttribute("quantita",$quantita_cibo);
my $new_area;
foreach my $temp (@area_list){
	if($temp){
			my $xpath_exp = "//zoo:cibo/zoo:area[.=\"$temp\"]";
			my $area_used = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
			if(!$area_used){
				$new_area = $doc->createElement("area");
				$new_area->appendTextNode($temp);
				$new_cibo->appendChild($new_area);
			}
	}
}
$root->appendChild($new_cibo);

my $doc2 = $parser->parse_string($root->toString());
my $xmlschema = XML::LibXML::Schema->new( location => "../xml/warehouse.xsd" );
if (eval { $xmlschema->validate( $doc2 ); } eq undef) {
	print $page->redirect(-URL=>"nuovo_cibo.cgi?error=Creazione cibo non riuscita - validazione xml fallita");
	exit;
}

open(XML,'>../xml/warehouse.xml') || file_error();
print XML $root->toString();
close(XML);

print $page->redirect( -URL => "gestione_magazzino.cgi");
exit;

sub file_error{
	print $page->redirect(-URL=>"nuovo_cibo.cgi?error=Inserimento in magazzino non riuscito - errore nella scrittura del file: $!");
	exit;
}
