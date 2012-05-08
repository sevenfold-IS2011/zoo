#!/usr/bin/perl


package partials;

use CGI;

sub header{
	print ' <div id="header">
						<div id="logo" class ="stripe">
							<h1>Monkey Island</h1>
							<p><i>Un&apos;esperienza selvaggia.. </i></p>
						</div>	
						<div id="nav">
							<ul class="nav">
								<li><a href="#">Chi siamo</a></li>
								<li><a href="#">Aree</a></li>
								<li><a href="animali.html">Animali</a></li>
								<li><a href="#">Servizi</a></li>
								<li><a href="#">Login dipendenti</a></li>
							</ul>
						</div>
					</div>'
}

sub footer{
	print '<div id="footer">
				   <p>Monkey Island S.r.l. | P.I. 0349034129384 | Via le man dae simie 32 | Curtarolo (PD)</p>
				 </div>'
}

sub _index{
	print '<div id="content">
				   <h3>I nostri eventi</h3>	
			  	 <dl>
					   <dt>Caccia al tesoro</dt>
						 <dd>Ogni primo sabato del mese, organizziamo per i pi&ugrave; piccoli una caccia al tesoro</dd>
						 <dt>L&apos;isola selvaggia</dt>
						 <dd>Ogni sabato sera, organizziamo serate tematiche con musica e drink</dd>
					 </dl>
				</div>';
}


sub prova{
	print 'prova';
}

1;