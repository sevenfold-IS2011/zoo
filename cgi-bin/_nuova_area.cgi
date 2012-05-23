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
 my $areaName=$input{"nome"};
 my $areaPos=$input{"posizione"};

my $zoo = XMLin('../xml/animals.xml');

#print $page->redirect( -URL => "nuova_area.cgi");

print $page->header,
			$page->start_html(-title => "Monkey Island || Lo zoo di Padova",
			 									-meta => {'keywords' => 'zoo padova animali monkey island',
																	'description' => 'sito ad utilizzo interno dello zoo Monkey Island di Padova',
																	'author' => '?????????'},
												-author => '?????????',
												-style=>{'src'=>'../css/master.css'});
partials::header();
print Dumper($zoo);
print $zoo->{area}->{1}->{animale}->[0]->{nome};

#my $id = @{ $zoo->{area}} + 1;
#push @{ $zoo->{area} }, { id => $5, nome => $areaName, posizione => $areaPos };

partials::footer();
print $page->end_html;
}

