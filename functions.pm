#!/usr/bin/perl

package functions;

use File::Spec;
use CGI::Session;


sub get_name_from_sid{
	$session = new CGI::Session(undef, $_[0], {File::Spec->tmpdir});
  return $session->param("name");
}



1;