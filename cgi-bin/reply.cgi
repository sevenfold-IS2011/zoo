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
		my $animal = $xpc -> findnodes("//zoo:animale[nome=\"$name\"]", $doc)->get_node(1);
		if (!$animal) {
			print $page->header();
			print '
						<h2>Richiesta errata - nessun animale con questo nome</h2>'; #nome univoco in tutto lo zoo o all'interno dell'area??
			exit;
		}
		my $area = $animal->getParent();
		$area->removeChild($animal); #non suicidi, ma figlicidi
		
		open(XML,'>../xml/animals.xml') || die("Cannot Open file $!");
		print XML $root->toString();
		close(XML);
		
		print $page->header();
		print Functions:animal_table;
		exit;
	}
	
	if ($action = "edit") {
		
		
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



