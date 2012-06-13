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
my $noscript = $page->param("noscript");
my $action = $page->param("action");

if($session->is_expired() || $session->is_empty()){
  print $page->header();
	if ($noscript eq "true") {
		print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
		exit;
	}
	
	print '
				<h2> Risorsa non accessibile - probabilmente la sessione è stata chiusa od è scaduta.</h2>
					<br />
				<h3> Si prega di rieffettuare il <a href="login.cgi">login </h3>';
	exit;
}

my $watDo = $page->param("watDo");

if ($watDo eq undef || (!$watDo eq "animals" && !$watDo eq "warehouse" && !$watDo eq "areas" && !$watDo eq "users") ){
	if ($noscript eq "true" || $action eq "update") {
		print $page->redirect( -URL => "area_privata.cgi?error=Richiesta errata - azione non definita.");
		exit;
	}
	print $page->header();
	print '
				<h3>Richiesta errata - parametro watDo incorretto</h3>';
	exit;
}

#------------------------------------------------------------------------ANIMALS
if ($watDo eq "animals")
{
	check_action();
	my $name = $page->param("name");
	my $parser = XML::LibXML->new;
	my $doc = $parser->parse_file("../xml/animals.xml");
	my $root = $doc->getDocumentElement();
	my $xpc = XML::LibXML::XPathContext->new;
	$xpc->registerNs('zoo', 'http://www.zoo.com');
	if (!$name) {
		if ($noscript eq "true" || $action eq "update") {
			print $page->redirect( -URL => "gestione_animali.cgi?error=Richiesta errata - nome non definito.");
			exit;
		}
		print $page->header();
		print '
					<h3>Richiesta errata - parametro nome indefinito</h3>';
		exit;
		}
	if ($action eq "destroy") {

		# hai un parametro noscript = true se devi ricomporre la pagina
		my $xpath_exp = "//zoo:animale[zoo:nome='".$name."']";
		my $animal = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		#my $asize = $xpc -> findnodes($xpath_exp, $doc)->size();
		if (!$animal) {
			if ($noscript eq "true") {
				print $page->redirect( -URL => "gestione_animali.cgi?error=Richiesta errata - animale non trovato.");
				exit;
			}
			print $page->header();
			print '
						<h3>Richiesta errata - animale non trovato</h3>';
			exit;
		}

		$xpath_exp = $xpath_exp."/zoo:img";
		my $image_path =  $xpc -> findnodes($xpath_exp, $doc)->get_node(1)->textContent();
		if($image_path){
			unlink($image_path);
		}

		my $area = $animal->parentNode();
		$area->removeChild($animal); #non suicidi, ma figlicidi

		open(XML,'>../xml/animals.xml') || file_error();
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

		my $xpath_exp = "//zoo:animale[zoo:nome='".$name."']";
		my $animal = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		if (!$animal) {
			print $page->redirect( -URL => "gestione_animali.cgi?error=Impossibile modificare l'animale - animale non trovato.");
			exit;
		}
		my $age = $page -> param("age");
		if (!isint($age)){
			print $page->redirect( -URL => "gestione_animali.cgi?error=Impossibile modificare l'animale - età non valida");
			exit;
		}
		my $gender = $page ->param("gender");
		if (!$gender || ($gender ne "Male" && $gender ne "Female")) {
			print $page->redirect( -URL => "gestione_animali.cgi?error=Impossibile modificare l'animale - sesso insensato");
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
			open (UPLOADFILE, ">$upload_dir/$filename" ) or file_error();
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
			open(XML,'>../xml/animals.xml') || file_error();
			print XML $root->toString();
			close(XML);
		}
		print $page->redirect(-URL => "gestione_animali.cgi");
		exit;
	}
}

#--------------------------------------------------------------------------USERS
if ($watDo eq "users") {
	check_action();
	my $username = $page->param("username");
	my $parser = XML::LibXML->new;
	my $doc = $parser->parse_file("../xml/workers.xml");
	my $root = $doc->getDocumentElement();
	my $xpc = XML::LibXML::XPathContext->new;
	$xpc->registerNs('zoo', 'http://www.zoo.com');
	if (!$username) {
		if ($noscript eq "true" || $action eq "update") {
			print $page->redirect( -URL => "gestione_utenti.cgi?error=Richiesta errata - nome non definito.");
			exit;
		}
		print $page->header();
		print '
					<h2>Richiesta errata - parametro username undefined</h2>';
		exit;
		}
	if ($action eq "destroy") {
		my $xpath_exp = "//zoo:username[. = \"$username\"]/..";
		my $user = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		if (!$user) {
			if ($noscript eq "true") {
				print $page->redirect( -URL => "gestione_utenti.cgi?error=Richiesta errata - utente non trovato.");
				exit;
			}
			print $page->header();
			print '
						<h2>Richiesta errata - nessun utente con questo nome</h2>';
			exit;
		}
		$user->parentNode()->removeChild($user);
		open(XML,'>../xml/workers.xml') || file_error();
		print XML $root->toString();
		close(XML);
		
		if ($noscript eq "true") {
			print $page->redirect(-URL => "gestione_utenti.cgi");
			exit;
		}
		print Functions::users_table();
		exit;
		}
	if ($action eq "update"){
		my $modified = undef;
		my $age = $page -> param("eta");
		my $find = ' ';
		my $replace = '';
		$find = quotemeta $find; # escape regex metachars if present
		$age =~ s/$find/$replace/g;
		if (!isint($age) || $age <= 0){
			print $page->redirect( -URL => "gestione_utenti.cgi?error=Richiesta errata - età insensata.");
			exit;
		}
		my $role = $page -> param("tipo");
		if (!$role || ($role ne "manager" && $role ne "impiegato")) {
			print $page->redirect( -URL => "gestione_utenti.cgi?error=Richiesta errata - tipo insensata.");
			exit
		}

		my $name = $page->param("nome");
		if (!$name){
			print $page->redirect( -URL => "gestione_utenti.cgi?error=Richiesta errata - nome indefinito.");
			exit
		}

		my $gender = $page -> param("sesso");
		if (!$gender || ($gender ne "M" && $gender ne "F")) {
			print $page->redirect( -URL => "gestione_utenti.cgi?error=Richiesta errata - genere insensato.");
			exit
		}

		my $current_role;
		if (Functions::is_manager_from_username($username)) {
			$current_role = "manager";
		} else {
			$current_role = "impiegato";
		}
		if (($role eq "manager" && $current_role eq "impiegato") ||
				($role eq "impiegato" && $current_role eq "manager")){
			$modified = 1;
			my $xpath_exp = "//zoo:".$current_role."[zoo:username='".$username."']";
			my $old_user_node = $xpc->findnodes($xpath_exp, $doc)->get_node(1);
			$old_user_node -> setNodeName($role);
		}

		my $xpath_exp = "//zoo:username[. = \"$username\"]/../zoo:nome";
		my $old_name_node = $xpc->findnodes($xpath_exp, $doc)->get_node(1);
		my $old_name = $old_name_node -> textContent();
		if ($old_name ne $name) {
			$modified = 1;
			my $new_name_node = $doc->createElement("nome");
			$new_name_node -> appendTextNode($name);
			$old_name_node -> replaceNode($new_name_node);
		}

		$xpath_exp = "//zoo:username[. = \"$username\"]/../zoo:sesso";
		my $old_gender_node = $xpc -> findnodes($xpath_exp,$doc)->get_node(1);
		my $old_gender = $old_gender_node -> textContent();
		if ($old_gender ne $gender) {
			$modified = 1;
			my $new_gender_node = $doc->createElement("sesso");
			$new_gender_node -> appendTextNode($gender);
			$old_gender_node -> replaceNode($new_gender_node);
		}

		$xpath_exp = "//zoo:username[. = \"$username\"]/../zoo:eta";
		my $old_age_node = $xpc -> findnodes($xpath_exp,$doc)->get_node(1);
		my $old_age = $old_age_node -> textContent();
		if ($old_age ne $age) {
			$modified = 1;
			my $new_age_node = $doc->createElement("eta");
			$new_age_node -> appendTextNode($age);
			$old_age_node -> replaceNode($new_age_node);
		}

		if($modified){
			open(XML,'>../xml/workers.xml') || file_error();
			print XML $root->toString();
			close(XML);
		}

		print $page->redirect(-URL => "gestione_utenti.cgi");
		exit;
	}

}

#----------------------------------------------------------------------WAREHOUSE
if ($watDo eq "warehouse"){
	my $cibo_id = $page->param("cibo");
	my $amount = $page->param("amount");
	check_action();
	if(!$cibo_id) {
		if ($noscript eq "true" || $action eq "update") {
			print $page->redirect( -URL => "gestione_magazzino.cgi?error=Richiesta errata - id non definito.");
			exit;
		}
		print $page->header();
		print '
					<h3>Richiesta errata - parametro id non definito</h3>';
		exit;
	}
	if ($action eq "add" || $action eq "remove" ) {
		if(!$amount || (!isint($amount) && !isfloat($amount)) || $amount < 0 ){# se $amount esiste, è > 0 e !(è un intero o un float)
			if ($noscript eq "true") {
				print $page->redirect( -URL => "gestione_magazzino.cgi?error=Richiesta errata - quantità non corretta.");
				exit;
			}
			print $page->header();
			print '
						<h3>Richiesta errata - quantità non corretta</h3>';
			exit;
		}
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
		open(XML,'>../xml/warehouse.xml') || file_error();
		print XML $root->toString();
		close(XML);

		if($noscript eq "true"){
			print $page->redirect( -URL => "gestione_magazzino.cgi");
		}
		print $page->header();
		print Functions::warehouse_table;

		exit;
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
		open(XML,'>../xml/warehouse.xml') || file_error();
		print XML $root->toString();
		close(XML);
		if($noscript){
			print $page->redirect( -URL => "gestione_magazzino.cgi");
		}
		print Functions::warehouse_table;
		exit;
	}
}

#--------------------------------------------------------------------------AREAS
if ($watDo eq "areas"){
	if($action eq "update"){#modifica area
		my $id = $page->param("id");
		my $area_nome = $page->param("nome");
		my $area_posizione = $page->param("posizione");
		my $area_cibo = $page->param("cibo");

		if(!$area_nome || isint($area_nome) || isfloat($area_nome)){
			print $page->redirect( -URL => "gestione_area.cgi?error=Richiesta errata - nome non definito o errato.");
			exit;
		}

		if(!$area_posizione || isint($area_posizione) || isfloat($area_posizione)){
			print $page->redirect( -URL => "gestione_area.cgi?error=Richiesta errata - posizione non definita o errata.");
			exit;
		}

		if(!$area_cibo || (!isint($area_cibo) && !isfloat($area_cibo) || $area_cibo < 0)){
			print $page->redirect( -URL => "gestione_area.cgi?error=Richiesta errata - quantità di cibo giornaliero non definita o errata.");
			exit;
		}

		my $find = ' ';
		my $replace = '';
		$find = quotemeta $find; # escape regex metachars if present
		$area_nome =~ s/$find/$replace/g;
		$area_posizione =~ s/$find/$replace/g;
		$area_cibo =~ s/$find/$replace/g;

		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/animals.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');
		my $xpath_exp = "//zoo:area[\@id=\"$id\"]";
		my $area = $xpc->findnodes($xpath_exp, $doc)->get_node(1);

		my $modified = undef;

		my $xpath_exp = "//zoo:area[\@id=\"$id\"]/\@nome";#old nome
		my $old_nome = $xpc->findnodes($xpath_exp, $doc)->get_node(1);
		if($area_nome ne $old_nome->getData()){
			my $nuovo_nome = $doc->createElement("nome");
			$nuovo_nome->appendTextNode($area_nome);
			$old_nome->parentNode->replaceChild($nuovo_nome,$old_nome);
			$modified = 1;
		}

		my $xpath_exp = "//zoo:area[\@id=\"$id\"]/\@posizione";#old posizione
		my $old_posizione = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		if($area_posizione ne $old_posizione->getData()){
			my $nuova_posizione = $doc->createElement("posizione");
			$nuova_posizione->appendTextNode($area_posizione);
			$old_posizione->parentNode->replaceChild($nuova_posizione,$old_posizione);
			$modified = 1;
		}

		my $xpath_exp = "//zoo:area[\@id=\"$id\"]/\@cibo_giornaliero";#old quantità di cibo
		my $old_cibo = $xpc -> findnodes($xpath_exp, $doc)->get_node(1);
		if($area_cibo ne $old_cibo->getData()){
			my $nuovo_cibo = $doc->createElement("cibo_giornaliero");
			$nuovo_cibo->appendTextNode($area_cibo);
			$old_cibo->parentNode->replaceChild($nuovo_cibo,$old_cibo);
			$modified = 1;
		}
		if($modified){
			open(XML,'>../xml/animals.xml') || file_error();
			print XML $root->toString();
			close(XML);
		}
		print $page->redirect( -URL => "gestione_area.cgi");
	}
	if($action eq "destroy"){
		my $id = $page->param("id");

		my $parser = XML::LibXML->new;
		my $doc = $parser->parse_file("../xml/animals.xml");
		my $root = $doc->getDocumentElement();
		my $xpc = XML::LibXML::XPathContext->new;
		$xpc->registerNs('zoo', 'http://www.zoo.com');
		
		my $xpath_exp = "//zoo:area[\@id=\"$id\"]";
		my $area = $xpc->findnodes($xpath_exp, $doc)->get_node(0);
		if (!$area) {
			print '<h2>Richiesta errata - nessua area ha questo id</h2>';
			exit;
		}
		else{
			my $xpath_exp = "//zoo:area[\@id=\"$id\"]/zoo:animale/zoo:img";#rimuovo le immagini degli animali che sono nell'area da cancellare
			my @image_path =  $xpc -> findnodes($xpath_exp, $doc);
			if(@image_path) {
				foreach my $temp (@image_path){
					unlink($temp->textContent());
				}
			}
			my $zoo = $area->parentNode();
			$zoo->removeChild($area);
			open(XML,'>../xml/animals.xml') || file_error();
			print XML $root->toString();
			close(XML);
		}

		my $doc = $parser->parse_file("../xml/warehouse.xml");#rimuovo dal magazzino il collegamento tra i cibi e le aree appena cancellate
		my $root = $doc->getDocumentElement();
		my $xpath_exp = "//zoo:area[.=\"$id\"]";
		my @area = $xpc->findnodes($xpath_exp, $doc);
		if(@area) {
			foreach my $temp (@area){
				my $parent = $temp->parentNode;
				$parent->removeChild($temp);
			}
		}
		open(XML,'>../xml/warehouse.xml') || file_error();
		print XML $root->toString();
		close(XML);

		if($noscript eq "true"){
			print $page->redirect( -URL => "gestione_area.cgi");
		}
		print $page->header();
		print Functions::animals_table;

		exit;
	}
}
sub check_action{
	if ($action eq undef || (!$action eq "destroy" && !$action eq "edit" && !$action eq "update")) {
		print $page->header();
		print '
					<h2>Richiesta errata - parametro action incorretto</h2>';
		exit;
	}
}

sub file_error{
	if ($noscript eq "true" || $action eq "update"){
		print $page->redirect(-URL=>"area_privata.cgi?error=Operazione fallita - errore nella scrittura del file: $!");
		exit;
	}
	print $page -> header();
	print "<h3>Operazione fallita - errore nella scrittura del file: $!</h3>";
	exit;
}


