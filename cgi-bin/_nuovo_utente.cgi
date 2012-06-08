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

my $name = $page->param("nome");
if (!$name){
	print $page->header();
	print '<h1> Non hai inserito il nome  (errori da sistemare)</h1>';
	exit;
}

my $username = $page->param("usernome");
if (!$username){
	print $page->header();
	print '<h1> Non hai inserito l\'username  (errori da sistemare)</h1>';
	exit;
}

if(username_taken($username)){
	print $page->header();
	print '<h1> username già preso (errori da sistemare)</h1>';
	exit;
}

my $password = $page->param("password");

if (!$password) {
	print $page->header();
	print '<h1> Non hai inserito la password  (errori da sistemare)</h1>';
	exit;
}

my $confirm = $page->param("password2");

if (!$password2) {
	print $page->header();
	print '<h1> Non hai inserito la conferma della password  (errori da sistemare)</h1>';
	exit;
}

if (!($password eq $password2)) {
	print $page->header();
	print '<h1> La password e la conferma non corrispondono  (errori da sistemare)</h1>';
	exit;
}

my $role = $page -> param("tipo");

if (!$role || (!($role eq "manager") && !($role eq "dipendente")) {
	print $page->header();
	print '<h1> Ruolo non corretto (errori da sistemare)</h1>';
	exit;
}










