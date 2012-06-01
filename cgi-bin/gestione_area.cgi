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
	print $page->header(-charset => 'utf-8'),
				$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
				 									-meta => {'keywords' => 'zoo padova animali monkey island',
																		'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																		'author' => '?????????'}, 
													-author => 'gaggi@math.unipd.it',
													-script=>[{-type=>'JAVASCRIPT', -src=>'../javascript/ajax.js'},{-type=>'javascript', -src=>'../javascript/gestione_aree.js'}],
													-style=>{'src'=>'../css/master.css'});
	partials::privateHeader($sid);
	my $watDo = "areas";
	partials::manageArea($sid, $watDo);					
	print $page->end_html;
}


exit;

