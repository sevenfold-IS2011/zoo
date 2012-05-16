#!/usr/bin/perl


use CGI;
use XML::LibXSLT;
use XML::LibXML;
use strict;
use warnings;

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



my $source = XML::LibXML->load_xml(location => 'xml/animals.xml');
my $nodeset = $source->find('//area[@id="01"]');
#my $nodeset = $source->find('//area');

#my @nodelist = $nodeset->get_nodelist;

#my $new_xml = XML::LibXML::Document->new( "1.0", "UTF-8");
#$new_xml->setDocumentElement($nodeset);

my $xslt = XML::LibXSLT->new();
my $style_doc = XML::LibXML->load_xml(location=>'xml/animal_template_embed.xsl', no_cdata=>1);
my $stylesheet = $xslt->parse_stylesheet($style_doc);
#my $results = $stylesheet->transform($source);
#my $results = $stylesheet->transform($nodeset);

#my $results = $stylesheet->transform($source, param => "'//area[@id=\"01\"]'");

#my $results = $stylesheet->transform($source, XML::LibXSLT::xpath_to_string(
#      -match=> '//area[@id=\"02\"]'
#      ));

my $results = $stylesheet->transform($source);


my $text = $stylesheet->output_as_bytes($results);	

my $find = '<?xml version="1.0"?>';
my $replace = "";
$find = quotemeta $find; # escape regex metachars if present

$text =~ s/$find/$replace/g;

print $text;
#print $new_xml->toString();
partials::footer();


print $page->end_html;
exit;

