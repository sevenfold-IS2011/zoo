#!/usr/bin/perl


package partials;

use functions;

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
					<img src="images/logo.png" width="300"/>
				</div>';
				
				
						
	
	if (!$_[0] eq undef){
		$name=functions::get_name_from_sid($_[0]);
		print "<p>Ciao $name !</p>";
	}
	print
	'</div>	
			<div id="nav">
				<ul class="nav">
					<li><a href="#">Chi siamo</a></li>
					<li><a href="#">Aree</a></li>
					<li><a href="animali.cgi">Animali</a></li>
					<li><a href="#">Servizi</a></li>
					<li><a href="login.cgi">Login dipendenti</a></li>
				</ul>
			</div>
		</div>	
		<div id="nav">
			<ul class="nav">
				<li><a href="#">Chi siamo</a></li>
				<li><a href="aree.html">Aree</a></li>
				<li><a href="animali.html">Animali</a></li>
				<li><a href="#">Servizi</a></li>
				<li><a href="#">Login dipendenti</a></li>
			</ul>
		</div>
	</div>';
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

sub login{
	print
	'<div id="login">
		 <h2>Per favore autenticarsi per l&apos;accesso all&apos;area riservata</h2>
		 <form action="_login.cgi" method="post" accept-charset="utf-8">
			 <label for="username">Username</label><input type="text" name="username" value="" placeholder="username"><br />
			 <label for="password">Password</label><input type="text" name="password" value=""placeholder="password">
			 <p><input type="submit" value="Authenticate &rarr;"></p>
		 </form>
	 </div>';
}

1;