#!/usr/bin/perl


package partials;
use strict;
use Functions;
use CGI;
use XML::LibXSLT;
use XML::LibXML;
use File::Slurp;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

sub login{
	if(!$_[0]){
		print
			'<div id="loginform">
				<form method="POST" action="/login.cgi">
			  	Username: <input type="text" name="username" size="15" /><br />
			  	Password: <input type="password" name="password" size="15" /><br />
			  	<div align="center">
			    	<p><input type="submit" value="Login" /></p>
			  	</div>
				</form>
			</div>';
	}else{
		print 'ciao utente loggato';
	}

}

sub header{
	my $sid = $_[0];
	my $error = $_[1];
	print
	' <div id="header">
  		<div id="logo">
				<div style="text-align:center;">
					<a href="index.cgi"><img src="../images/logo.png" width="300" alt="logo"/></a>
				</div>';
	print
	'</div>
			<div id="nav">
				<ul class="nav">
					<li class="item"><a href="chi-siamo.cgi">Chi siamo</a></li>
					<li class="item"><a href="area.cgi">Aree</a></li>
					<li class="item"><a href="animali.cgi">Animali</a></li>
					<li class="item"><a href="servizi.cgi">Servizi</a></li>';
	if (!$sid){
					print '<li class="item"><a href="login.cgi">Login dipendenti</a></li>';
				}else{
					print '<li class="item"><a href="area_privata.cgi">Area privata</a></li>';
				}
	print'
				</ul>
			</div>';
	if($error){
	print 	'<div class="errors"><p>'.$error.'</p></div>'	;
	}
	print '</div>	';
}

sub footer{
	print '
	<div id="footer">
    <p>Monkey Island S.r.l. | P.I. 0349034129384 | Via le man dae simie 32 | Curtarolo (PD) | <a href="mappa.html">mappa del sito</a> <br />
	    <a href="http://validator.w3.org/check?uri=referer"><img
	      src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Transitional" height="31" width="88" /></a>
	  </p>
  </div>'
}

sub _index{
	print
	'<div id="content">
     <h3>I nostri eventi</h3>
  	 <dl>
	     <dt>Caccia al tesoro</dt>
		   <dd>Ogni primo sabato del mese, organizziamo per i pi&ugrave; piccoli una caccia al tesoro</dd>
		   <dt>L&apos;isola selvaggia</dt>
		   <dd>Ogni sabato sera, organizziamo serate tematiche con musica e drink</dd>
	 	 </dl>
	</div>';
}

sub animali{
	print Functions::rendered_template("../xml/animals.xml", "../xml/external_animals_template.xsl");
}

sub animale{
	print
	'<div id = "content">
		<div class="animale">
			<img class="animal" src='.Functions::get_animal_img($_[0]).' />
			<div class="testo">
				<h4>Scheda:</h4>
				<p>Nome: '.$_[0].'</p>
				<p>Età: '.Functions::get_animal_age($_[0]).'</p>
				<p>Sesso: '.Functions::get_animal_gender($_[0]).'</p>
				<h4>Storia:</h4>
			</div>
		</div>
	 </div>';
}

sub servizi{
	print
	'<div id="content">
		<a href="#accessibilita"><img src="../images/icons/handicap.png"  alt="icona handicap" /></a> 
		<a href="#pronto-soccorso"><img src="../images/icons/first-aid.png"  alt="icona pronto soccorso" /></a>
		<a href="#accoglienza"><img src="../images/icons/parking.png"  alt="icona parcheggio" /></a>
		<a href="#ristoro><img src="../images/icons/snack-bar.png" " alt="icona snack bar" /></a>
		<a href="#bus"><img src="../images/icons/bus-service.png"  alt="icona servizio bus" /></a>
		<h3>I nostri servizi</h3>
		<h4 id="eventi">Eventi</h4>
		<p>Il nostro personale è preparato alla gestione di ogni tipo di eventi. Se la tua famiglia festeggia qualche evenienza particolare, mettiti in contatto con la nostra gestione eventi per organizzare al meglio la vostra giornata!</p>
		<h4 id="accoglienza">Accoglienza gruppi</h4>
		<p>Lo zoo prevede uno sconto per grandi gruppi di visitatori. E&apos; attrezzato inoltre con un parcheggio per bus e vengono organizzati su richiesta guide turistiche specializzate che offriranno alla vostra comitiva la loro conoscenza sulle specie e la loro vita selvatica. Per ulteriori informazioni visitare la pagina <a href="contatti.html">contatti</a>
		<h4 id="bus">Servizio bus</h4>
		<p>Lo zoo è collegato via bus alla città di Padova e ai suoi punti di maggior interesse.</p>
		<h4 id="pronto-soccorso">Primo soccorso</h4>
		<p>Disponiamo di personale qualificato a intervenire in caso di malessere dei nostri clienti. Siamo attrezzati a norma di legge per sopperire alle necessità sanitarie in attesa dell\'eventuale arrivo di personale medico professionale</p>
		<h4 id="sicurezza">Sicurezza</h4>
		<p>Il nostro zoo è conforme a tutte le normative europee in materia di sicurezza. Gli animali pericolosi sono gestiti da personale preparato secondo processi professionali. Le nostre attrezzature sono le più moderne nel mercato e garantiscono la sicurezza del personale, dei visitatori e degli animali.</p>
		<h4 id="ristoro">Ristoro</h4>
		<p>All\'interno dello zoo è possibile trovare vari punti di ristoro e fontane d\'acqua potabile gratuite.</p>
		<h4 id="accessibilita">Accessibilità</h4>
		<p>Lo zoo è attrezzato per accogliere tutti, dai grandi ai piccini senza dimenticare le persone con difficoltà a deambulare.
		In particolare abbiamo: <br />
		<ul>
			<li>Servizi igienici attrezzati con fasciatoio</li>
			<li>Servizi igienici per portatori di handicap</li>
			<li>Rampe su tutti i dislivelli architettonici</li>
			<li>Servizio touchscreen su totem per l&apos;accesso alle informazioni dello zoo</li>
			<li>Mini club</li>
			<li>Fontane disperse per il parco per le giornate di calura</li>
		</ul>    
	</div>'
}

sub login{
	print
	'<div id="login">
		 <h2>Per favore autenticarsi per l&apos;accesso all&apos;area riservata</h2>
		 <form action="_login.cgi" method="post" accept-charset="utf-8">
			 <label for="username">Username</label><input type="text" name="username" value="" placeholder="username"><br />
			 <label for="password">Password</label><input type="password" name="password" value=""placeholder="password">
			 <p><input type="submit" value="Authenticate &rarr;"></p>
		 </form>
	 </div>';
}

sub area{
	my $areaId = $_[0];
	if ($areaId){
		my $source = XML::LibXML->load_xml(location => '../xml/animals.xml');
		my $xslt = XML::LibXSLT->new();
		my $xslt_string =  read_file('../xml/animal_template_embed.xsl');
		my $find = 'test="@id="';
		my $replace = "test=\"\@id=$areaId\"";
		$find = quotemeta $find; # escape regex metachars if present
		$xslt_string =~ s/$find/$replace/g;
		open(new_xml_file,">../xml/animal_template_embed_$areaId.xsl") or die "Can't create file: $!";
		print new_xml_file $xslt_string;
		close(new_xml_file);
		my $style_doc = XML::LibXML->load_xml(location=>"../xml/animal_template_embed_$areaId.xsl", no_cdata=>1);
		my $stylesheet = $xslt->parse_stylesheet($style_doc);
		my $results = $stylesheet->transform($source);
		my $text = $stylesheet->output_as_bytes($results);
		$find = '<?xml version="1.0"?>';
		$replace = "";
		$find = quotemeta $find; # escape regex metachars if present
		$text =~ s/$find/$replace/g;
		print $text;
	} else {
		print Functions::rendered_template("../xml/animals.xml", "../xml/external_area_template.xsl");
	}
}
=mascio
sub areaList{
	my @stuff = @_;
	my $item;
	my $j = 0;
	foreach $item (@stuff){
		if ($j % 2 eq 0){
			print "<li><a href= area.cgi?id=$item>";
		}else{
			print "Area $item</a></li>";
		}
		$j = $j + 1;
	}
}
=cut
sub userForm{
	my $action = $_[0];
	if($action eq "new"){
		print'<div id="content">
			<h2>Gestione utenti</h2>
			<p>Da questo pannello è possibile aggiungere, rimuovere o modificare gli utenti che hanno accesso all&apos;area privata del sito.</p>
			<h2>Creazione nuovo utente</h2>
			<form action="gestione-utenti_submit" method="post" accept-charset="utf-8">
				<label for="username">Username</label><input type="text" name="username" value="" id="username" placeholder="Username">
				<label for="password">Password</label><input type="password" name="password" value="" id="password" placeholder="Password">
				<label for="password_confirmation">Conferma password</label><input type="password" name="password_confirmation" value="" id="password_confirmation" placeholder="Ripeti password">

				<p><input type="submit" value="Crea &rarr;"></p>
			</form>
			</div>';
	}
#qua altri elsif a cascata



}

sub chi_siamo{
   	print
	'<div id="content">
		<h3>Il nostro zoo</h3>
		<h4>Location</h4>
		<p>Situato nel mezzo della campagna veneta, lo zoo Mokey Island garantisce comodità di parcheggio e accoglienza per tutta la famiglia.</p>
		<h4>Gli inizi</h4>
		<p>Nato nel 1990 da un\'idea di Pinco Pallo lo zoo offre momenti indimenticabili per tutta la famiglia. </p>
		<h4>Segreteria clienti:</h4>
		<p><strong>045-593755<br /><a mailto="info@monkeyisland.it">info@monkeyisland.it</a></strong></p>
	</div>' 
}
sub privateHeader{
	my $error = $_[0];
	print '<div id="header">
		<div id="logo">
			<div style="text-align:center;">
				<a href= "area_privata.cgi"><img src="../images/logo-privato.png" width="300" alt = "logo privato"/></a>
			</div>
		</div>
		<div id="nav">
			<ul class="nav">
				<li class="item"><a href="chi-siamo.cgi">Chi siamo</a></li>
				<li class="item"><a href="area.cgi">Aree</a></li>
				<li class="item"><a href="animali.cgi">Animali</a></li>
				<li class="item"><a href="servizi.cgi">Servizi</a></li>
				<li class="item"><a href="logout.cgi">Logout</a></li>
			</ul>
		</div>
	</div>';
	if ($error) {
		print '
		<div class="errors"><p>'.$error.'</p></div>';
	}
	

}

sub privateArea{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right"><h4>Per favore utilizzare il menù a sinistra per accedere all\'area desiderata</h4></div>';
	footer();
	print '</div>';
}

sub manageArea{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right">';
	print Functions::area_table;
	print '</div>';
	footer();
	print '</div>';
}

sub editArea{
	my $area_name = Functions::get_areaName_from_id($_[2]);
	my $area_posizione = Functions::get_areaPosizione_from_id($_[2]);
	my $area_cibo = Functions::get_areaCibo_from_id($_[2]);
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '
	<div id = "right">
		<h4>Modifica area '.$area_name.'</h4>
		<div class = "form-wrapper">
			<form action="reply.cgi" method="post" accept-charset="utf-8" enctype="multipart/form-data">
			<input type="hidden" name="watDo" value="areas">
			<input type="hidden" name="action" value="update">';
			print "<input type=\"hidden\" name=\"id\" value=\"$_[2]\">
			  <fieldset>
			    <label for=\"name\">Nome: </label><input type=\"text\" name=\"nome\" value=\"$area_name\"><br/>
			    <label for=\"posizione\">Posizione: </label><input type=\"text\" name=\"posizione\" value=\"$area_posizione\"><br/>
			    <label for=\"cibo\">Cibo giornaliero (Kg): </label><input type=\"text\" name=\"cibo\" value=\"$area_cibo\"><br/>
			    <p><input type=\"submit\" value=\"modifica area\"></p>";
			    print '
			  </fieldset>
			</form>
		</div>
	</div>';
	footer();
	print '</div>';
}

sub newArea{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '
	<div id = "right">
		<h3>Nuova Area</h3>
		<div class = "form-wrapper">
			<form action="_nuova_area.cgi" method="post" accept-charset="utf-8">
			  <fieldset>
			    <label for="name">Nome</label><input type="text" name="nome" value="" placeholder="nome"><br />
			    <label for="posizione">Posizione</label><input type="text" name="posizione" value="" placeholder="posizione">
			    <label for="cibo">Cibo giornaliero (Kg)</label><input type="text" name="cibo" value="" placeholder="quantità">
			    <p><input type="submit" value="Crea Area"></p>
			  </fieldset>
			</form>
		</div>
	</div>';
	footer();
	print '</div>';
}

sub updateWarehouse{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '	<div id = "right">
		<h4>Aggiungi tipologia di cibo:</h4>
		<div class = "form-wrapper">
			<form action="_nuovo_cibo.cgi" method="post" accept-charset="utf-8">
			  <label for="nome">Nome: </label><input type="text" name="nome" value="" placeholder="Nome" />
			  <label for="quanitita">Quantita: </label><input type="text" name="quantita" value="" placeholder="Quantita" />';
				areaCheckbox(Functions::get_areas);
				print '
			  <p><input type="submit" value="Aggiungi"/></p>
			</form>
		</div>
	</div>';

	footer;
	print '</div>';
}

sub manageWarehouse{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right">';
	print Functions::warehouse_table();
	print '</div>';
	footer();
	print '</div>';
}

sub manageUsers{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right">';
	print Functions::users_table($_[0]);
	print '</div>';
	footer();
	print '</div>';
}


sub newUser{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '
	<div id = "right">
		<h3>Nuovo Utente</h3>
		<div class = "form-wrapper">
			<form action="_nuovo_utente.cgi" method="post" accept-charset="utf-8">
			  <fieldset>
			  <label for="tipo">Tipo</label><select name="tipo"><option value="impiegato">Impiegato</option><option value="manager">Manager</option></select><br />
			  <label for="nome">Nome</label><input type="text" name="nome" value="" placeholder="Nome e cognome"><br />
			  <label for="sesso">Sesso</label><select name="sesso"><option value="M">M</option><option value="F">F</option></select><br />
			  <label for="eta">Et&agrave;</label><input type="text" name="eta" value=""><br />
			  <label for="username">Username</label><input type="text" name="username" value="" placeholder="Username"><br />
			  <label for="password">Password</label><input type="password" name="password" value="" placeholder="Password">
			  <label for="password">Conferma </label><input type="password" name="password2" value="" placeholder="Una diversa da prima">
			  <p><input type="submit" value="Crea Utente"></p>
			  </fieldset>
			</form>
		</div>
	</div>';
	footer();
	print '</div>';
}

sub editAnimal{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	my $gender = Functions::get_animal_gender($_[2]);
	print '<div id = "right"> <h3>Modifica '.$_[2].'</h3>
		<div class = "form-wrapper">
			<form action="reply.cgi" method="post" accept-charset="utf-8" enctype="multipart/form-data">
			<input type="hidden" name="watDo" value="animals">
			<input type="hidden" name="action" value="update">
				<fieldset>
			  	<label for="nome">nome: </label><input type="text" name="name" id="nome" value="'.$_[2].'" readonly/><br />';

	if ($gender eq "Male"){
		print '	<label for="sesso">sesso: </label><select name="gender" id="sesso">
							<option value="Male" default>M</option>
							<option value="Female">F</option>
						</select><br />';
	} elsif ($gender eq "Female") {
		print '
						<label for="sesso">sesso: </label><select name="gender" id="sesso">
							<option value="Male">M</option>
							<option value="Female"default>F</option>
						</select><br />';
	}
	my $age = Functions::get_animal_age($_[2]);
	print'
					<label for="eta">et&agrave;: </label><input type="text" name="age"  value="'.$age.'" id="eta"/><br />
			  	<label for="image">Foto (non selezionarne nessuna se non vuoi sostituirla):</label> <input type="file" name="image" value="carica foto" id="image"/><br />
			  	<p><input type="submit" value="Modifica animale" /></p>
				</fieldset>
			</form>
		</div> </div>';
		footer();
		print '</div>';
}

sub editPassword{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '
	<div id = "right">
		<h3>Modifica password</h3>
		<div class = "form-wrapper">
			<fieldset>
				<form action="_modifica_password.cgi" method="post" accept-charset="utf-8">
			  	<label for="old_password">Vecchia password</label><input type="password" name="old_password" value="" placeholder="Vecchia password"><br />
			  	<label for="password">Nuova password</label><input type="password" name="password" value="" placeholder="Nuova password">
			  	<label for="password_confirm">Conferma nuova Password:</label><input type="password" name="password_confirm" value="" placeholder="Nuova password">
			  	<p><input type="submit" value="Modifica password"></p>
				</form>
			</fieldset>
		</div>
	</div>';
	footer();
	print '</div>';
}

sub manageAnimals{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right">';
	print Functions::animal_table();
	print '</div>';
	footer();
	print '</div>';
}

sub newAnimal{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);

	print '<div id = "right"> <h3>Nuovo animale:</h3>
		<div class = "form-wrapper">
			<form action="_nuovo_animale.cgi" method="post" accept-charset="utf-8" enctype="multipart/form-data">
				<fieldset>
					<label for="area">area</label><select name="area" id="area">';
	areaSelect(Functions::get_areas);
	print '
					</select><br/>
			  	<label for="nome">nome: </label><input type="text" name="nome" id="nome"/><br />
			  	<label for="sesso">sesso: </label><select name="sesso" id="sesso">
						<option value="Male">M</option>
						<option value="Female">F</option>
					</select><br />
			  	<label for="eta">et&agrave;: </label><input type="text" name="eta"  placeholder="5" id="eta"/><br />
			  	<label for="image">foto:</label> <input type="file" name="image" value="carica foto" id="image"/><br />
			  	<p><input type="submit" value="Aggiungi animale" /></p>
				</fieldset>
			</form>
		</div> </div>';
		footer();
		print '</div>';
}

sub areaSelect{
	my @stuff = @_;
	my $item;
	my $j = 0;
	foreach $item (@stuff){
		if ($j % 2 eq 0){
			print "<option value=\"$item\">";
		}else{
			print "Area $item</option>";
		}
		$j = $j + 1;
	}
}

sub areaCheckbox{
	my @stuff = @_;
	my $size = scalar @stuff;
	print "<div class=\"checkbox\">Aree:<br>";
	for(my $k = 0 ; $k < $size ; $k = $k + 1){
		my $id = @stuff[$k];
		my $name = @stuff[$k+1];
		print "<input  type=\"checkbox\" name=\"$id\" value=\"$id\"/>$name<br>";
		$k = $k + 1;
	}
	print '</table></div>';
}


sub noscript{
	print '<noscript>
	                <meta http-equiv="Refresh" content="1;url='.$_[0].'" />
	       </noscript>';
}

sub privateMenu{
	my $sid = $_[0];
	my $watDo =$_[1];
	print
				'<div id ="left">
					<ul>
				  	<li><a href="gestione_area.cgi">Gestione Aree</a></li>';
	if ($watDo eq "areas"){
		print'
						<ul>
							<li><a href="nuova_area.cgi">Nuova Area</a></li>
						</ul>';

					}
	print'		<li><a href="gestione_magazzino.cgi">Gestione Magazzino</a></li>';
	if ($watDo eq "warehouse"){
		print'
						<ul>
							<li><a href="nuovo_cibo.cgi">Aggiungi cibo</a></li>
						</ul>';

					}
	print'    <li><a href="gestione_animali.cgi">Gestione Animali</a></li>';
	if ($watDo eq "animals"){
		print'
						<ul>
							<li><a href="nuovo_animale.cgi">Inserisci animale</a></li>
						</ul>';
	}
	print'<li><a href="gestione_utenti.cgi">Gestione Utenti</a></li>';
	if (Functions::is_manager($sid)){
		if ($watDo eq "users"){
			print'
							<ul>
								<li><a href="nuovo_utente.cgi">Inserisci utente</a></li>
								<li><a href="modifica_password.cgi">Modifica password</a></li>
							</ul>';
		}
	}
	print'
					</ul>
				</div>';
}

sub newUser{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '
	<div id = "right">
		<h3>Nuovo Utente</h3>
		<div class = "form-wrapper">
			<form action="_nuovo_utente.cgi" method="post" accept-charset="utf-8">
			  <fieldset>
			  <label for="tipo">Tipo</label><select name="tipo"><option value="impiegato">Impiegato</option><option value="manager">Manager</option></select><br />
			  <label for="nome">Nome</label><input type="text" name="nome" value="" placeholder="Nome e cognome"><br />
			  <label for="sesso">Sesso</label><select name="sesso"><option value="M">M</option><option value="F">F</option></select><br />
			  <label for="eta">Et&agrave;</label><input type="text" name="eta" value=""><br />
			  <label for="username">Username</label><input type="text" name="username" value="" placeholder="Username"><br />
			  <label for="password">Password</label><input type="password" name="password" value="" placeholder="Password">
			  <label for="password">Conferma </label><input type="password" name="password2" value="" placeholder="Una diversa da prima">
			  <p><input type="submit" value="Crea Utente"></p>
			  </fieldset>
			</form>
		</div>
	</div>';
	footer();
	print '</div>';
}

sub edit_user{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	my $is_manager = Functions::is_manager_from_username($_[2]);
	my $gender = Functions::get_user_gender($_[2]);
	my $name = Functions::get_user_name($_[2]);
	my $age = Functions::get_user_age($_[2]);
	print '
	<div id = "right">
		<h3>Modifica Utente</h3>
		<div class = "form-wrapper">
			<form action="reply.cgi" method="post" accept-charset="utf-8">
				<input type="hidden" name="watDo" value="users">
				<input type="hidden" name="action" value="update">
				<input type="hidden" name="username" value="'.$_[2].'">
			  <fieldset>
			  	<label for="tipo">Tipo</label>';
	if ($is_manager){
		print'<select name="tipo">
							<option value="impiegato">Impiegato</option>
							<option value="manager" selected = "selected">Manager</option>
					</select>'
	}else{
		print'<select name="tipo">
							<option value="impiegato" selected = "selected">Impiegato</option>
							<option value="manager">Manager</option>
					</select>'
	}
	print
					'<br />
			  	<label for="nome">Nome</label><input type="text" name="nome" value="'.$name.'" ><br />
			  	<label for="sesso">Sesso</label>
					<select name="sesso">';
	if ($gender eq "Male"){
		print '
						<option value="M" selected="selected">M</option>
						<option value="F">F</option>';
	} else {
		print '
						<option value="M">M</option>
						<option value="F" selected="selected">F</option>';
	}
	print '
					</select><br />
			  	<label for="eta">Et&agrave;</label><input type="text" name="eta" value="'.$age.'"><br />
			  	<p><input type="submit" value="Modifica Utente"></p>
			  </fieldset>
			</form>
		</div>
	</div>';
	footer();
	print '</div>';
}
1;

