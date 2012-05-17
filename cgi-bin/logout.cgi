#!/usr/bin/perl
use strict;
use CGI;
use CGI::Session;
use File::Spec;

my $page = new CGI;
my $sid = $page->cookie("CGISESSID") || undef;

if (!$sid eq undef){
	my $session = new CGI::Session(undef, $_[0], {File::Spec->tmpdir});
	$session -> delete();
}
print $page->redirect( -URL => "animali.cgi");
exit;