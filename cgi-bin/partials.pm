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
	print
	' <div id="header">
  		<div id="logo">
				<div style="text-align:center;">
					<a href="index.cgi"><img src="../images/logo.png" width="300" alt="logo"/></a>
				</div>';

	if (!$_[0] eq undef){
	  my $name=Functions::get_name_from_sid($_[0]);
		if($name){
			print "<p>Ciao $name !</p>";
			print '<p><a href="logout.cgi">Logout</a></p>';
		}
	}

	print
	'</div>
			<div id="nav">
				<ul class="nav">
					<li class="item"><a href="#">Chi siamo</a></li>
					<li class="item"><a href="area.cgi">Aree</a></li>
					<li class="item"><a href="animali.cgi">Animali</a></li>
					<li class="item"><a href="#">Servizi</a></li>
					<li class="item"><a href="login.cgi">Login dipendenti</a></li>
				</ul>
			</div>
		</div>	';
}

sub footer{
	print '
	<div id="footer">
    <p>Monkey Island S.r.l. | P.I. 0349034129384 | Via le man dae simie 32 | Curtarolo (PD)</p>
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
	print
	'<div id="content">
		<h3>I nostri animali</h3>
		<dl>
			<dt><a href="animali/orangotango.html">Orangotango</a></dt>
				<dd>Pretto in due parole orango e tango</dd>
			<dt><a href="animali/maiale.html">Maiale</a></dt>
				<dd>Siamo uno zoo e i maiali non ci dovrebbero essere. Ma sono ottimi da mangiare allora ogni tanto copemo el mascio.</dd>
			<dt><a href="animali/struzzo.html">Struzzo</a></dt>
				<dd>Un oseo a caso e se magna i so ovi.</dd>
		</dl>
	</div>'
}

sub servizi{
	print
	'<div id="content">
		<h3>I nostri servizi</h3>
		<h4>Eventi</h4>
		<p>Il nostro personale è preparato alla gestione di ogni tipo di eventi. Se la tua famiglia festeggia qualche evenienza particolare, mettiti in contatto con la nostra gestione eventi per organizzare al meglio la vostra giornata!</p>
		<h4>Accoglienza gruppi</h4>
		<p>Lo zoo prevede uno sconto per grandi gruppi di visitatori. E&apos; attrezzato inoltre con un parcheggio per bus e vengono organizzati su richiesta guide turistiche specializzate che offriranno alla vostra comitiva la loro conoscenza sulle specie e la loro vita selvatica. Per ulteriori informazioni visitare la pagina <a href="contatti.html">contatti</a>
		<h4>Sicurezza</h4>
		<p>Il nostro zoo è conforme a tutte le normative europee in materia di sicurezza. Gli animali pericolosi sono gestiti da personale preparato secondo processi professionali. Le nostre attrezzature sono le più moderne nel mercato e garantiscono la sicurezza del personale, dei visitatori e degli animali.</p>
		<h4>Accessibilità</h4>
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
		print '<div id="content">
			<h3>Il nostro parco</h3>
			<p>All&apos;interno dello spazio dedicato ai visitatori &egrave; possibile visitare il percorso safari o a piedi. Si possono trovare zone di ristoro e divertimento per i pi&ugrave; piccoli.</p>
			<h3>Mappa</h3>
			<div class="figure">
				<img src="../images/map.png">
				<p>La mappa del parco Monkey Island</p>
			</div>
			<div class="list">
				<h3>Aree dello Zoo:</h3>';
			areaList(Functions::get_areas);
			print'
			</div>
		</div>';
	}
}


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


sub privateHeader{
	print '<div id="header">
		<div id="logo">
			<div style="text-align:center;">
				<a href= "area_privata.cgi"><img src="../images/logo-privato.png" width="300" alt = "logo privato"/></a>
			</div>
		</div>
		<div id="nav">
			<ul class="nav">
				<li class="item"><a href="#">Chi siamo</a></li>
				<li class="item"><a href="area.cgi">Aree</a></li>
				<li class="item"><a href="animali.cgi">Animali</a></li>
				<li class="item"><a href="#">Servizi</a></li>
				<li class="item"><a href="logout.cgi">Logout</a></li>
			</ul>
		</div>
	</div>';
}

sub privateArea{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right"> CONTENUTO </div>';
	footer;
	print '</div>';
}

sub manageArea{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right"> CONTENUTO </div>';
	footer;
	print '</div>';

}

sub newArea{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '
	<div id = "right">
		<h3>Nuova Area</h3>
		<div class = form>
			<form action="_nuova_area.cgi" method="post" accept-charset="utf-8">
			  <label for="name">Nome</label><input type="text" name="nome" value="" placeholder="nome"><br />
			  <label for="posizione">Posizione</label><input type="text" name="posizione" value="" placeholder="">
			  <p><input type="submit" value="Crea Area"></p>
			</form>
		</div>
	</div>';
	footer;
	print '</div>';
}

sub manageUsers{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right"> CONTENUTO </div>';
	footer;
	print '</div>';

}

sub manageAnimals{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);
	print '<div id = "right"> CONTENUTO </div>';
	footer;
	print '</div>';

}

sub newAnimal{
	print '<div id = "content">';
	privateMenu($_[0], $_[1]);

	print '<div id = "right"> <h3>Nuovo animale:</h3>
		<div class = "form-wrapper">
			<form action="_nuovo_animale.cgi" method="post" accept-charset="utf-8" enctype="multipart/form-data">
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
			</form>
		</div> </div>';
		footer;
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
							<li><a href="#">Visualizza Area</a></li>
						</ul>';

					}
	print'    <li><a href="gestione_animali.cgi">Gestione Animali</a></li>';
	if ($watDo eq "animals"){
		print'
						<ul>
							<li><a href="#">Gestisci animali</a></li>
							<li><a href="nuovo_animale.cgi">Inserisci animale</a></li>
						</ul>';
	}
	print'		<li><a href="#">Gestione Magazzino</a></li>
						<li><a href="gestione_utenti.cgi">Gestione Utenti</a></li>';
	if ($watDo eq "users"){
		print'
						<ul>
							<li><a href="#">Gestisci utenti</a></li>
							<li><a href="#">Inserisci utente</a></li>
						</ul>';
	}
	print'
					</ul>
				</div>';
}



1;

