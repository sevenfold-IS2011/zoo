#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;

$CGI::POST_MAX = 1024 * 5000;

my $page = new CGI; 
my $sid = $page->cookie("CGISESSID") || undef;
if (!$sid){
  print $page->redirect( -URL => "login.cgi");
	exit;
}

if (!is_manager($sid)){
  print $page->redirect( -URL => "area_privata.cgi");
	exit;
}

