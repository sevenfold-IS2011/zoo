#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;

$page = new CGI;
$sid = $page->cookie("CGISESSID") || undef;

if (!$sid eq undef){
	$session = new CGI::Session(undef, $_[0], {File::Spec->tmpdir});
	$session -> delete();
}
print $page->redirect( -URL => "animali.cgi");
exit;