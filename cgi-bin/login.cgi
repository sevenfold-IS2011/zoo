#!/usr/bin/perl
use strict;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;

my $page = new CGI;
print $page->header(-charset => 'utf-8'),
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova || Login",
												-head => $page->Link({-rel => 'shortcut icon',
																					 -href => '../favicon.ico',
																					 -type => 'image/x-icon'}),
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-class => "login",
												-style=>{'src'=>'../css/master.css'});
my $error = $page -> param("error") || undef;
partials::header(undef, $error);
partials::login();					
partials::footer();
							

print $page->end_html;
exit;

