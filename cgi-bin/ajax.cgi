#!/usr/bin/perl
use strict;
use warnings;


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
my $page = new CGI;
my $sid = $page->cookie("CGISESSID") || undef;

if ($sid eq undef){
	print $page->header();
	print '
				<h2> Risorsa non accessibile - probabilmente la sessione è stata chiusa od è scaduta.</h2>
					<br />
				<h3> Si prega di rieffettuare il <a href="login.cgi">login </h3>';
	exit;
}
my $watDo = $page->param("watDo");

if ($watDo eq undef || (!$watDo eq "animals" && !$watDo eq "warehouse" && !$watDo eq "areas" && !$watDo eq "users") ){
	print $page->header();
	print '
				<h2>Richiesta errata - parametro watDo incorretto</h2>';
	exit;
}

if ($watDo eq "animals")
{
	my $action = $page->param("action");
	check_action($action);
	if ($action eq "destroy") {
		my $name = $page->param("name");
		if (!$name) {
			print $page->header();
			print '
						<h2>Richiesta errata - parametro name incorretto</h2>';
			exit;
		}
		
	}
	
}








sub check_action{
	my $action = $_[0];
	if ($action eq undef || (!$action eq "destroy" && !$action eq "edit" && !$action eq "update")) {
		print $page->header();
		print '
					<h2>Richiesta errata - parametro action incorretto</h2>';
		exit;
	}
}