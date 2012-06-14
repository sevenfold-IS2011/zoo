#!/usr/bin/perl
use strict;


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
my $page = new CGI;
print $page->header(-charset => 'utf-8'),
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'},
												-author => '?????????',
												-class => "aree",
												-style=>{'src'=>'../css/master.css'});
my $session = CGI::Session->load();
my $sid = $session->id();
my $animal = $page -> param("name") || undef;
partials::header($sid, "area");
partials::area(CGI::param('id'));
partials::footer();


print $page->end_html;
exit;

