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
		$new_area = $doc->createElement("area");
		$new_area->appendTextNode($temp);
		$new_cibo->appendChild($new_area);
	}
}
$root->appendChild($new_cibo);
open(XML,'>../xml/warehouse.xml') || die("Cannot Open file $!");
print XML $root->toString();
close(XML);

print $page->redirect( -URL => "gestione_magazzino.cgi");
exit;

