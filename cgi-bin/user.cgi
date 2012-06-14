#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);


use CGI;
use partials;
my $page = new CGI;
print $page->header,
			$page->start_html(-dtd => ['-//W3C//DTD XHTML 1.0 Strict//EN', "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"],
												-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-style=>{'src'=>'../css/master.css'});
my $session = CGI::Session->load();
my $sid = $session->id();
partials::header($sid);
partials::user(CGI::param('action'));					
partials::footer();
							

print $page->end_html;
exit;

