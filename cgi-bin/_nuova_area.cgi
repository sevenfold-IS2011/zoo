#!/usr/bin/perl
use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

use partials;
use XML::Simple;
use Data::Dumper;

my $buffer;
my $name;
my $value;
my %input;
my $pair;
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
my @pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	 $value =~ tr/+/ /;
	 $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/g;
	 $name =~ tr/+/ /;
	 $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/g;
	 $input{$name} = $value;
}

my $page = new CGI;

	my $sid = $page->cookie("CGISESSID") || undef;
if (!$sid){
  print $page->redirect( -URL => "login.cgi");
}else{
 my $areaName = $input{"nome"};
 my $areaPos = $input{"posizione"};

print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'},
												-author => '?????????',
												-style=>{'src'=>'../css/master.css'});
partials::header();

#my $zoo = XMLin('../xml/animals.xml', forcearray=>1, KeyAttr=>{});#forcearray per avere tutto in array
#print Dumper($zoo);
#print $zoo->{area}->{1}->{animale}->[0]->{nome}->[0];
#$zoo = {'area'=>{'1'=>{'nome'=>'scimmie','posizione'=>'nord'},} };
#print Dumper($zoo);

#push @{$zoo->{area}},{'area'=>{'1'=>{'nome'=>'scimmie','posizione'=>'nord'},} };

#my $simple = new XML::Simple();
#$simple->XMLout($zoo, OutputFile => 'prova.xml',);

#-----------meglio così credo
my $parser = XML::LibXML->new;
my $doc = $parser->parse_file('../xml/animals.xml');
my $root = $doc->getDocumentElement();

my $new_element= $doc->createElement("area");
$new_element->setAttribute( 'id', 5 );
$new_element->setAttribute( 'nome', $areaName );
$new_element->setAttribute( 'posizione', $areaPos );

$root->appendChild($new_element);

print $root->toString(1);

#-----------
partials::footer();
print $page->end_html;
}

