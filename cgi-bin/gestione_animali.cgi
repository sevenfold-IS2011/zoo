#!/usr/bin/perl
use strict;
use warnings;


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
my $page = new CGI;
my $sid = $page->cookie("CGISESSID") || undef;
if (!$sid){
  print $page->redirect( -URL => "login.cgi");
}else{
	my $noscript = $page -> param("noscript") || "false";  
	print $page->header(-charset => 'utf-8'),
				$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
				 									-meta => {'keywords' => 'zoo padova animali monkey island',
																		'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																		'author' => '?????????'}, 
													-author => 'gaggi@math.unipd.it',
													-script=>[{-type=>'JAVASCRIPT', -src=>'../javascript/ajax.js'},
															  {-type=>'javascript', -src=>'../javascript/gestione_animali.js'},
															  {-type=>'javascript', -src=>'../javascript/images.js'},],
	   											-style=>{'src'=>'../css/master.css'});
												if ($noscript eq "false") {
													partials::noscript("gestione_animali.cgi?noscript=true"); 
												}
	partials::privateHeader($sid);
	my $watDo = "animals";
	partials::manageAnimals($sid, $watDo, $noscript);					
	print $page->end_html;
}


exit;

