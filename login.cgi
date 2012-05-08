#!/usr/bin/perl

use CGI;
use partials;
$page = new CGI;
print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-style=>{'src'=>'css/master.css'});
partials::header();
partials::login();					
partials::footer();
							

print $page->end_html;
exit;

