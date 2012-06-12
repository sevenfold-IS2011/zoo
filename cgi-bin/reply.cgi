#!/usr/bin/perl
use strict;
use warnings;


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
use XML::LibXML;
use Scalar::Util::Numeric qw(isint isfloat);
use File::Spec;
use File::Basename;

$CGI::POST_MAX = 1024 * 5000;


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

		# hai un parametro noscript = true se devi ricomporre la pagina
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
			exit;
		}

		print $page->header();
		print Functions::animal_table;
		exit;
	}

	if ($action eq "edit") {
		print $page->redirect('modifica_animale.cgi?name='.$name);
		exit;
	}

	if ($action eq "update") {
		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/animals.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');
		my $xpath_exp = "//zoo:animale[zoo:nome='".$name."']";
		my $animal = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		if (!$animal) {
			print $page->header();
			print '
						<h2>Richiesta errata - nessun animale con questo nome</h2>';
			exit;
		}
		my $age = $page -> param("age");
		if (!isint($age)){
			print $page->header();
			print '
						<h2>Richiesta errata - Età non valida</h2>';
			exit;
		}
		my $gender = $page ->param("gender");
		if (!$gender || ($gender ne "Male" && $gender ne "Female")) {
			print $page->header();
			print '
						<h2>Richiesta errata - Sesso non valido</h2>';
			exit;
		}
		my $find = ' ';
		my $replace = '';
		$find = quotemeta $find; # escape regex metachars if present
		$age =~ s/$find/$replace/g;
		$xpath_exp = "//zoo:animale[zoo:nome='".$name."']/zoo:eta";
		my $old_age_node = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		my $old_age = $old_age_node -> nodeValue();
		$old_age =~ s/$find/$replace/g;

		my $modified = undef;

		if($age ne $old_age){
			$modified = 1;
			my $new_age_node = $doc->createElement("eta");
			$new_age_node ->appendTextNode($age);
			$old_age_node ->replaceNode($new_age_node);
		}
		$xpath_exp = "//zoo:animale[zoo:nome='".$name."']/zoo:sesso";
		my $old_gender_node = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		my $old_gender = $old_gender_node -> nodeValue();

		if($gender ne $old_gender){
			$modified = 1;
			my $new_gender_node = $doc->createElement("sesso");
			$new_gender_node -> appendTextNode($gender);
			$old_gender_node -> replaceNode($new_gender_node);
		}

		my $filename = $page->param("image");

		if($filename){
			my $upload_dir = "../images/animals";
			my ($fname, $path, $extension) = fileparse($filename, '\..*');
			$filename = $fname.$extension;

			#manca un check sull'image name, occhio

			my $upload_filehandle = $page->upload("image");
			open (UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
			binmode UPLOADFILE;
			while (<$upload_filehandle>){
				print UPLOADFILE;
			}
			close UPLOADFILE;

			$xpath_exp = "//zoo:animale[zoo:nome='".$name."']/zoo:img";
			my $old_image_node = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
			my $old_image_path = $old_image_node -> textContent();
			if($old_image_path){
				unlink($old_image_path);
			}
			$modified = 1;
			my $new_image_node = $doc->createElement("img");
			my $image_path = $upload_dir.'/'.$filename;
			$new_image_node -> appendTextNode($image_path);
			$old_image_node -> replaceNode($new_image_node);
		}

		if($modified){
			open(XML,'>../xml/animals.xml') || die("Cannot Open file $!");
			print XML $root->toString();
			close(XML);
		}
		print $page->redirect(-URL => "gestione_animali.cgi");
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
	my $cibo_id = $page->param("cibo");
	my $amount = $page->param("amount");
	check_action($action);
	if(!$action) {
		print $page->header(-charset => 'utf-8');
		print '<h2>Richiesta errata - azione non esistente</h2>';
		exit;
	}
	if(!$cibo_id) {
		print $page->header(-charset => 'utf-8');
		print '<h2>Richiesta errata - parametro cibo non definito</h2>';
		exit;
	}
	if(!$amount | ( !isint($amount) && !isfloat($amount) | $amount < 0 )){# se $amount esiste, è > 0 e !(è un intero o un float)
		print $page->header(-charset => 'utf-8');
		print '<h3>Richiesta errata - "quantità" inserita non correttamente, deve essere un numero positivo</h3>';
		exit;
	}
	if ($action eq "add" | $action eq "remove" ) {
		print $page->header(-charset => 'utf-8');

		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/warehouse.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');

		my $xpath_exp = "//zoo:cibo[\@id=\"$cibo_id\"]/\@nome";#prendo il nome del cibo
		my $nome = $xpc->findnodes($xpath_exp, $doc)->get_node(1);

		$xpath_exp = "//zoo:cibo[\@id=\"$cibo_id\"]/\@quantita";#prendo la quantità del cibo
		my $quantita = $xpc->findnodes($xpath_exp, $doc)->get_node(1);

		$xpath_exp = "//zoo:cibo[\@id=\"$cibo_id\"]/zoo:area";
		my $arealist = $xpc->findnodes($xpath_exp, $doc);

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
		$cibo->replaceNode($new_cibo);
		$root->appendChild($new_cibo);#appendo il nuovo cibo
		open(XML,'>../xml/warehouse.xml') || die("Cannot Open file $!");
		print XML $root->toString();
		close(XML);

		if($noscript){
			print $page->redirect( -URL => "gestione_magazzino.cgi");
		}
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
		if($noscript){
			print $page->redirect( -URL => "gestione_magazzino.cgi");
		}
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

