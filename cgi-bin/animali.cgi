#!/usr/bin/perl


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
$page = new CGI;
print $page->header(-charset => 'utf-8'),
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-style=>{'src'=>'../css/master.css'});
my $sid = $page->cookie("CGISESSID") || undef;
partials::header($sid);
partials::animali();					
partials::footer();
							

print $page->end_html;
exit;

