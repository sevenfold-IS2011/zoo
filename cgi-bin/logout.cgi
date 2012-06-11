#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use File::Spec;

my $page = new CGI;
my $sid = $page->cookie("CGISESSID") || undef;

if ($sid){
	my $session = new CGI::Session(undef, $sid, {File::Spec->tmpdir});
	$session -> delete();
}
print $page->redirect( -URL => "index.cgi");
exit;