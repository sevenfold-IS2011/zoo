#!/usr/bin/perl
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
use strict;
use warnings;
my $page = new CGI;
print $page->header(-charset => 'utf-8'),
			$page->start_html(-dtd => ['-//W3C//DTD XHTML 1.0 Strict//EN', "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"],
												-title => "Monkey Island || Lo zoo di Padova || Animali",
												-head => $page->Link({-rel => 'shortcut icon',
																					 -href => '../favicon.ico',
																					 -type => 'image/x-icon'}),
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => 'LeChuck’s crew'},  
												-class => "animali",
												-style=>{'src'=>'../css/master.css'});
my $session = CGI::Session->load();
my $sid = $session->id();
my $animal = $page -> param("name") || undef;
partials::header($sid);
if ($animal){
  partials::animale($animal);  
}
else{
	partials::animali();
} 			
partials::footer();
							

print $page->end_html;
exit;

