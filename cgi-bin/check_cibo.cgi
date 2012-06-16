#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
my $page = new CGI;
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
	exit;
}
my $sid = $session->id();
print $page->header(-charset => 'utf-8'),
			$page->start_html(-dtd => ['-//W3C//DTD XHTML 1.0 Strict//EN', "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"],
												-title => "Monkey Island || Lo zoo di Padova || Magazzino - Controllo disponibilità",
												-head => $page->Link({-rel => 'shortcut icon',
																					 -href => '../favicon.ico',
																					 -type => 'image/x-icon'}),
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-script=>[{-type=>'javascript', -src=>'../javascript/ajax.js'},
														  {-type=>'javascript', -src=>'../javascript/gestione_animali.js'},
														  {-type=>'javascript', -src=>'../javascript/images.js'},],
												-style=>{'src'=>'../css/master.css'});
my $error = $page -> param("error") || undef;
partials::privateHeader($error);
my $watDo = "warehouse";

my $days = $page -> param("giorni") || undef;

partials::check_food($sid, $watDo, $days);					
print $page->end_html;

exit;