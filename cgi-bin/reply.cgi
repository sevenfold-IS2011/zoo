#!/usr/bin/perl
use strict;
use warnings;


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
use XML::LibXML;



my $page = new CGI;
my $sid = $page->cookie("CGISESSID") || undef;

if ($sid eq undef){
	print $page->header();
	print '
				<h2> Risorsa non accessibile - probabilmente la sessione è stata chiusa od è scaduta.</h2>
					<br />
				<h3> Si prega di rieffettuare il <a href="login.cgi">login </h3>';
	exit;
}
my $watDo = $page->param("watDo");

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

		print $page->header();
		print Functions::animal_table;
		exit;
	}

	if ($action == "edit") {
		use CGI;
		my $query=new CGI;
		print $query->redirect('modifica_animale.cgi?name='.$name);
	exit;
	}

	if ($action == "update") {
	# aggiorna xml
	exit;
	}
}

if ($watDo == "users") {
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

if ($watDo eq "users"){
	my $action = $page->param("action");
	check_action($action);
	my $username = $page->param("username");
	if (!$username) {
		print $page->header();
		print '
					<h2>Richiesta errata - parametro name undefined</h2>';
		exit;
		}
	if ($action eq "destroy") {

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

