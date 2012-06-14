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

my $area_id = $page -> param("id");
if (!$area_id){
	print $page->redirect(-URL=>"gestione_area.cgi?error=Modifica area fallita - area non specificata");
	exit;
}
my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
my $size = $xp->find("//area[\@id=\"$area_id\"]")->size();
if ($size < 1){
	print $page->redirect(-URL=>"gestione_area.cgi?error=Modifica area fallita - area non trovata");
	exit;
}

print $page->header,
			$page->start_html(-dtd => ['-//W3C//DTD XHTML 1.0 Strict//EN', "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"],
												-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'},
												-author => '?????????',
												-style=>{'src'=>'../css/master.css'});
my $error = $page -> param("error") || undef;
partials::privateHeader($error);
my $watDo = "areas";
partials::editArea($sid, $watDo, $area_id );
print $page->end_html;

exit;

