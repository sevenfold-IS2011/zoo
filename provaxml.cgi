#!/usr/bin/perl


use CGI;
use XML::LibXSLT;
use XML::LibXML;

use partials;
$page = new CGI;
print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'}, 
												-author => 'gaggi@math.unipd.it',
												-style=>{'src'=>'css/master.css'});
$sid = $page->cookie("CGISESSID") || undef;
if ($sid eq undef){
	print 'sid undef';
}else{
	print "sid= $sid";
}
partials::header();


my $xslt = XML::LibXSLT->new();

my $source = XML::LibXML->load_xml(location => 'xml/animal_0.xml');
my $style_doc = XML::LibXML->load_xml(location=>'xml/animal_template.xsl', no_cdata=>1);
my $stylesheet = $xslt->parse_stylesheet($style_doc);
my $results = $stylesheet->transform($source);
print $stylesheet->output_as_bytes($results);	
partials::footer();


print $page->end_html;
exit;

