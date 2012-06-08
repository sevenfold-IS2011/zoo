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

if ($watDo eq "warehouse"){
	my $action = $page->param("action");
	check_action($action);
	my $cibo_id = $page->param("cibo");
	print $page->header();
	if(!$cibo_id) {
		print '
					<h2>Richiesta errata - parametro cibo non definit</h2>';
		exit;
	}
	my $amount = $page->param("amount");
	#TO DO: controllare che $amount sia un double
	if ($action eq "add") {
		print "vuoi aggiungere $amount al cibo $cibo_id";
	}
	if ($action eq "remove") {
		print "vuoi rimuovere $amount al cibo $cibo_id";
	}
	if ($action eq "destroy") {
		print "vuoi distruggere il cibo $cibo_id";
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

