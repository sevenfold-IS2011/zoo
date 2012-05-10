#!/usr/bin/perl


use CGI;
use XML::LibXSLT;
use XML::LibXML;
use strict;

use partials;
my $page = new CGI;
print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-style=>{'src'=>'css/master.css'});
my $sid = $page->cookie("CGISESSID") || undef;

partials::header();


my $xslt = XML::LibXSLT->new();

my $source = XML::LibXML->load_xml(location => 'xml/animals.xml');
my $style_doc = XML::LibXML->load_xml(location=>'xml/animal_template_embed.xsl', no_cdata=>1);
my $stylesheet = $xslt->parse_stylesheet($style_doc);
my $results = $stylesheet->transform($source);
my $text = $stylesheet->output_as_bytes($results);	


my $find = '<?xml version="1.0"?>';
my $replace = "";
$find = quotemeta $find; # escape regex metachars if present

$text =~ s/$find/$replace/g;

print $text;
partials::footer();


print $page->end_html;
exit;

