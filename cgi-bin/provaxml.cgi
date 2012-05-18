#!/usr/bin/perl


use CGI;
use XML::LibXSLT;
use XML::LibXML;
use strict;
use warnings;
use File::Slurp;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

use partials;
my $page = new CGI;
print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-style=>{'src'=>'../css/master.css'});
my $sid = $page->cookie("CGISESSID") || undef;

partials::header();



my $source = XML::LibXML->load_xml(location => '../xml/animals.xml');
#my $nodeset = $source->find('//area[@id="01"]');
#my $nodeset = $source->find('//area');
#my @nodelist = $nodeset->get_nodelist;
#my $new_xml = XML::LibXML::Document->new( "1.0", "UTF-8");
#$new_xml->setDocumentElement($nodeset);

my $xslt = XML::LibXSLT->new();

#my $xslt_file;
#open xslt_file, 'xml/animal_template_embed.xsl' or die "Couldn't open file: $!"; 

my $xslt_string =  read_file('../xml/animal_template_embed.xsl');
#print $xslt_string; 

my $find = 'test="@id=02"';
my $replace = 'test="@id=01"';
$find = quotemeta $find; # escape regex metachars if present
$xslt_string =~ s/$find/$replace/g;

open(new_xml_file,'>../xml/animal_template_embed_01.xsl') or die "Can't create file: $!";
print new_xml_file $xslt_string;
close(new_xml_file);






my $style_doc = XML::LibXML->load_xml(location=>'../xml/animal_template_embed_02.xsl', no_cdata=>1);
my $stylesheet = $xslt->parse_stylesheet($style_doc);
#my $results = $stylesheet->transform($source);
#my $results = $stylesheet->transform($nodeset);

#my $results = $stylesheet->transform($source, param => "'//area[@id=\"01\"]'");

#my $results = $stylesheet->transform($source, XML::LibXSLT::xpath_to_string(
#      -match=> '//area[@id=\"02\"]'
#      ));

my $results = $stylesheet->transform($source);


my $text = $stylesheet->output_as_bytes($results);	

$find = '<?xml version="1.0"?>';
$replace = "";
$find = quotemeta $find; # escape regex metachars if present

$text =~ s/$find/$replace/g;

print $text;
#print $new_xml->toString();
partials::footer();


print $page->end_html;
exit;

