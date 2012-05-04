#!/usr/bin/perl



use CGI;
$page = new CGI;
print $page->header, $page->start_html("ciao semo!"), $page->h1("semo"), $page->end_html;
