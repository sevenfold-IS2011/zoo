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
print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'},
												-author => '?????????',
												-style=>{'src'=>'../css/master.css'});
partials::privateHeader($sid);
my $watDo = "areas";
partials::editArea($sid, $watDo, $page->param("id") );
print $page->end_html;

exit;

