#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::XPath;
use partials;
my $page = new CGI;
my $session = CGI::Session->load();
if($session->is_expired() || $session->is_empty()){
  print $page->redirect( -URL => "login.cgi?error=Sessione scaduta o inesistente. Prego rieffettuare il login.");
	exit;
}
my $sid = $session->id();

my $animal_name = $page -> param("name");
if (!$animal_name){
	print $page->redirect(-URL=>"gestione_animali.cgi?error=Modifica animale fallita - animale non specificato");
	exit;
}
my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
my $size = $xp->find("//animale[nome=\"$animal_name\"]")->size();
if ($size < 1){
	print $page->redirect(-URL=>"gestione_animali.cgi?error=Modifica animale fallita - animale non trovato");
	exit;
}

print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'},
												-author => '?????????',
												-style=>{'src'=>'../css/master.css'});
my $error = $page -> param("error") || undef;
partials::privateHeader($error);
my $watDo = "animals";

partials::editAnimal($sid, $watDo, $animal_name);
print $page->end_html;

exit;

