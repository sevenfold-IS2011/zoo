#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
my $page = new CGI;
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi");
	exit;
}
my $sid = $session->id();
print $page->header(-charset => 'utf-8'),
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova || Gestione animali",
												-head => $page->Link({-rel => 'shortcut icon',
												 											-href => '../favicon.ico',
												 											-type => 'image/x-icon'}),
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => 'LeChuck’s crew'},  
												-script=>[{-type=>'JAVASCRIPT', -src=>'../javascript/ajax.js'},
														  {-type=>'javascript', -src=>'../javascript/gestione_animali.js'},
														  {-type=>'javascript', -src=>'../javascript/images.js'},],
												-style=>{'src'=>'../css/master.css'});
my $error = $page -> param("error") || undef;
partials::privateHeader($error);
my $watDo = "animals";

partials::manageAnimals($sid, $watDo);					
print $page->end_html;



exit;

