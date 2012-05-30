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
	print "There was a problem uploading your photo (try a smaller file). Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
	}
my $area = $page->param("area");
if(!Functions::area_exists($area)){
	print $page->header();
	print "Area non esistente. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}
my $name = $page->param("nome");
if(Functions::name_in_area_taken($area, $name)){
	print $page->header();
	print "Nome già presoin quell'area. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}
my $gender = $page->param("sesso");
if($gender != "Female" && $gender !="Male"){
	print $page->header();
	print "Gender insensato. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}

my $age = $page->param("eta");
my $find = ' ';
my $replace = '';
$find = quotemeta $find; # escape regex metachars if present
$age =~ s/$find/$replace/g;

if ($age < 0 || $age > 150){ # bisogna fare il controllo o con una regexp o con scalar::utils
	print $page->header();
	print "age insensato. Questi errori andranno gestiti con un div apposito nella pagina precedente";
	exit;
}



print $page->header();
print "Area $area, nome $name, genere $gender e età $age";

exit;

