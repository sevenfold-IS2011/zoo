#!/usr/bin/perl

package functions;


sub get_name_from_sid{
	$session = new CGI::Session("driver:File", $_[0], {File::Spec->tmpdir});
	return $session->param("name");
}



1;