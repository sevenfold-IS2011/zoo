#!/usr/bin/perl
use strict;
use warnings;


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
use XML::LibXML;



my $page = new CGI;
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->header();
	print '
				<h2> Risorsa non accessibile - probabilmente la sessione è stata chiusa od è scaduta.</h2>
					<br />
				<h3> Si prega di rieffettuare il <a href="login.cgi">login </h3>';
	exit;
}

my $watDo = $page->param("watDo");
my $noscript = $page->param("noscript");

if ($watDo eq undef || (!$watDo eq "animals" && !$watDo eq "warehouse" && !$watDo eq "areas" && !$watDo eq "users") ){
	print $page->header();
	print '
				<h2>Richiesta errata - parametro watDo incorretto</h2>';
	exit;
}

#------------------------------------------------------------------------ANIMALS
if ($watDo eq "animals")
{
	my $action = $page->param("action");
	check_action($action);
	my $name = $page->param("name");
	if (!$name) {
		print $page->header();
		print '
					<h2>Richiesta errata - parametro name undefined</h2>';
		exit;
		}
	if ($action eq "destroy") {
		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/animals.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');
		my $xpath_exp = "//zoo:animale[zoo:nome='".$name."']";
		my $animal = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		#my $asize = $xpc -> findnodes($xpath_exp, $doc)->size();
		if (!$animal) {
			print $page->header();
			print '
						<h2>Richiesta errata - nessun animale con questo nome</h2>';
			#print "il nome era: $name, ho trovato $asize nodi, xpath era $xpath_exp"; #nome univoco in tutto lo zoo o all'interno dell'area??
			exit;
		}

		$xpath_exp = $xpath_exp."/zoo:img";
		my $image_path =  $xpc -> findnodes($xpath_exp, $doc)->get_node(1)->textContent();
		if($image_path){
			unlink($image_path);
		}

		my $area = $animal->parentNode();
		$area->removeChild($animal); #non suicidi, ma figlicidi

		open(XML,'>../xml/animals.xml') || die("Cannot Open file $!");
		print XML $root->toString();
		close(XML);

		if ($noscript eq "true") {
			$page->redirect(-URL => "gestione_animali.cgi");
		}

		print $page->header();
		print Functions::animal_table;
		exit;
	}

	if ($action eq "edit") {
		my $query=new CGI;
		print $query->redirect('modifica_animale.cgi?name='.$name);
	exit;
	}

	if ($action eq "update") {
	# aggiorna xml
	exit;
	}
}

#--------------------------------------------------------------------------USERS
if ($watDo eq "users") {
	my $action = $page->param("action");
	check_action($action);
	my $username = $page->param("username");
	if (!$username) {
		print $page->header();
		print '
					<h2>Richiesta errata - parametro username undefined</h2>';
		exit;
		}
	if ($action eq "destroy") {
		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/workers.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');
		my $xpath_exp = "//zoo:employee[zoo:username='".$username."'] | //zoo:manager[zoo:username=']".$username."']";
		my $user = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		#my $asize = $xpc -> findnodes($xpath_exp, $doc)->size();
		if (!$user) {
			print $page->header();
			print '
						<h2>Richiesta errata - nessun animale con questo nome</h2>';
			#print "il nome era: $name, ho trovato $asize nodi, xpath era $xpath_exp"; #nome univoco in tutto lo zoo o all'interno dell'area??
			exit;
		}
		print $page->header();
		print 'l\'ho trovato';
		}

}

#----------------------------------------------------------------------WAREHOUSE
if ($watDo eq "warehouse"){
	my $action = $page->param("action");
	check_action($action);
	my $cibo_id = $page->param("cibo");
	if(!$cibo_id) {
	  print $page->header();
		print '<h2>Richiesta errata - parametro cibo non definit</h2>';
		exit;
	}
	my $amount = $page->param("amount");
	#--------------------TO DO: controllare che $amount sia un double
	if ($action eq "add" | $action eq "remove" ) {
		print $page->header(-charset => 'utf-8');
		#print "vuoi aggiungere $amount al cibo $cibo_id";

		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/warehouse.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');

		my $xpath_exp = "//zoo:cibo[\@id=\"$cibo_id\"]/\@nome";#prendo il nome del cibo
		my $nome = $xpc->findnodes($xpath_exp, $doc)->get_node(0);
		#print $nome->getData;

		$xpath_exp = "//zoo:cibo[\@id=\"$cibo_id\"]/\@quantita";#prendo la quantità del cibo
		my $quantita = $xpc->findnodes($xpath_exp, $doc)->get_node(0);
		#print $quantita->getData;

		$xpath_exp = "//zoo:cibo[\@id=\"$cibo_id\"]/zoo:area";#perchè non funziona?
		my $arealist = $xpc->findnodes($xpath_exp, $doc);
		my $size = $xpc->findnodes($xpath_exp, $doc)->size;

		my $new_cibo = $doc->createElement("cibo");
		my $new_area;
		$new_cibo->setAttribute("id",$cibo_id);
		$new_cibo->setAttribute("nome",$nome->getData);
		my $new_quantita;
		if ($action eq "add") {
			$new_quantita = $quantita->getData + $amount;
		}
		else{
			if ($action eq "remove") {
				$new_quantita = $quantita->getData - $amount;
			}
		}
		$new_cibo->setAttribute("quantita",$new_quantita);
		my $temp;
		my $size = $arealist->size;
		for(my $count = 1; $count <= $size ; $count = $count+1){
			$temp = $arealist->get_node($count);
			$new_area = $doc->createElement("area");#creo il nuovo cibo
			$new_area->appendTextNode($temp->textContent);
			$new_cibo->appendChild($new_area);
		}

		my $xpath_exp = "//zoo:cibo[\@id='".$cibo_id."']";#rimuovo il vecchio cibo
		my $cibo = $xpc->findnodes($xpath_exp, $doc)->get_node(0);
		#my $zoo = $cibo->parentNode();
		#$zoo->replaceChild($new_cibo, $cibo);
		$cibo->replaceNode($new_cibo);


		$root->appendChild($new_cibo);#appendo il nuovo cibo
		open(XML,'>../xml/warehouse.xml') || die("Cannot Open file $!");
		print XML $root->toString();
		close(XML);

		print Functions::warehouse_table;
	}
	if ($action eq "destroy") {
		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/warehouse.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');
		my $xpath_exp = "//zoo:cibo[\@id='".$cibo_id."']";
		my $cibo = $xpc->findnodes($xpath_exp, $doc)->get_node(0);
		if (!$cibo) {
			print '<h2>Richiesta errata - nessun cibo ha questo id</h2>';
			exit;
		}
		my $zoo = $cibo->parentNode();
		$zoo->removeChild($cibo);
		open(XML,'>../xml/warehouse.xml') || die("Cannot Open file $!");
		print XML $root->toString();
		close(XML);
		print Functions::warehouse_table;
		exit;
	}
}

sub check_action{
	my $action = $_[0];
	if ($action eq undef || (!$action eq "destroy" && !$action eq "edit" && !$action eq "update")) {
		print $page->header();
		print '
					<h2>Richiesta errata - parametro action incorretto</h2>';
		exit;
	}
}

