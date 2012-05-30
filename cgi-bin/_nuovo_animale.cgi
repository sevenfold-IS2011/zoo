#!/usr/bin/perl

use CGI;
use CGI::Session;
use File::Spec;
use Functions;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;


$CGI::POST_MAX = 1024 * 5000;
my $upload_dir = "/images/animals";

my $page = new CGI; 
my $filename = $page->param("image"); 
if (!$filename){ 
	print $page->header();
	print "There was a problem uploading your photo (try a smaller file).";
	exit;
	}
my $name = $page->param("nome");
my $gender = $page->param("sesso");
my $age = $page->param("eta");



print $page->header();
print "Ho fatto cose";

exit;

