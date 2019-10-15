#!/usr/bin/perl

use strict;
use warnings;
use Time::Piece;
use Math::Round;
use DateTime;
use DateTime::Format::Strptime;

############################################################################
# A script to create tweets for a progress bar bot
# Made by Simon Meier-Vieracker, @fussballinguist, www.fussballlinguistik.de
############################################################################

# --> Adjust the beginning and end of the semester
my $begin = '14.10.2019\t07:30:00';
my $end = '07.02.2020\t20:00:00';

#############################
# No changes below this line!
#############################

my $format = '%d.%m.%Y\t%T';
my $period = Time::Piece->strptime($end, $format)
		 - Time::Piece->strptime($begin, $format);
my $percent = $period / 100;
my $strp = DateTime::Format::Strptime->new(
    pattern => '%d.%m.%Y\t%T'
);
my $dt = $strp->parse_datetime($begin);
for (my $var = 1; $var < 101; $var++) {
	my $p = round($var / 10);
	printf "%s", $dt->add(seconds => $percent)->strftime("%d.%m.%Y\t%T\t");
	my $diff = 10 - $p;
	print "\\\\o\/\\n";
	print "▓" x $p;
	print "░" x $diff;
	print "\\n$var\% des Semesters sind rum!\n";	
}
