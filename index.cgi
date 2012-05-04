#!/usr/bin/perl


use CGI;
$page = new CGI;
print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-style=>{'src'=>'css/master.css'});
print '											<div id="header">
															<div id="logo" class="stripe">
																<h1>Monkey Island</h1>
																<p><i>Un&apos;esperienza selvaggia.. </i></p>
															</div>	
															<div id="nav">
																<ul class="nav">
																	<li><a href="#">Chi siamo</a></li>
																	<li><a href="#">Aree</a></li>
																	<li><a href="#">Animali</a></li>
																	<li><a href="#">Servizi</a></li>
																	<li><a href="#">Login dipendenti</a></li>
																</ul>
															</div>
														</div>

														<div id="content">
															<div id>
																<h2>Monkey Island</h2>
																<p>Benvenuti sullo spazio virtuale dedicato a <i>Monkey Island</i>, lo zoo più misterioso del triveneto</p>
															</div>

															<h3>I nostri eventi</h3>
															<dl>
																<dt>Caccia al tesoro</dt>
																	<dd>Ogni primo sabato del mese, organizziamo per i più piccoli una caccia al tesoro</dd>
																<dt>L&apos;isola selvaggia</dt>
																	<dd>Ogni sabato sera, organizziamo serate tematiche con musica e drink</dd>
															</dl>
														</div>

														<div id="footer">
															<p>Monkey Island S.r.l. | P.I. 0349034129384 | Via le man dae simie 32 | Curtarolo (PD)</p>
														</div>';												

print $page->end_html;
exit;
