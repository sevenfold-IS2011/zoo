#!/usr/bin/perl
use strict;
use warnings;


use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use partials;
my $page = new CGI;
my $sid = $page->cookie("CGISESSID") || undef;