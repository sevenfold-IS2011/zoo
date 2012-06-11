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
  print $page->redirect( -URL => "login.cgi");
	exit;
}
my $sid = $session->id();
print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'},
												-author => '?????????',
												-style=>{'src'=>'../css/master.css'});
partials::privateHeader($sid);
my $watDo = "animals";
my $animal_name = $page -> param("name");
my $area = $page -> param("area");

if (!$animal_name || !$area){
	print $page -> header();
	print "<h1> Nome animale o area non presenti</h1>";
	exit;
}
my $xp = XML::XPath->new(filename=>'../xml/animals.xml');
my $size = $xp->find("//area[\@id=$area]/animale[nome=\"$animal_name\"]")->size();

if (size < 1){
	print $page -> header();
	print "<h1> Animale richiesto non trovato</h1>";
	exit;
}
partials::editAnimal($sid, $watDo, $page->param("name"), $page->param("area"));
print $page->end_html;

exit;

