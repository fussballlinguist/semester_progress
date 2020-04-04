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
my $begin = '06.04.2020\t07:30:00';
my $end = '17.07.2020\t20:00:00';

#############################
# No changes below this line!
#############################

my @ints = ("\\\\o\/","Mein lieber Herr Gesangsverein!","Scheiß die Wand an!","Alter Schwede!","Heidewitzka!","Holla die Waldfee!","WTF!!","Ach du grüne Neune!","Sapperlot!","Ich glaub, mein Schwein pfeift!","Heiliger Bimbam!","Prost Mahlzeit!","Da brat mir einer n Storch!","Ach nu meine Nase!","Hör mir auf!","Mannometer!","Ist es zu glauben?","Oh my fucking goodness!","Lecko mio!","Alter!","Gopferdeggl!","Grundgütiger!","Krass!","Juhuu!","Echt jetzt?","Tschakka!","Derbst, Alter!","Gimme five!","Da legst di nieda!","Eieiei!","Heiliger Strohsack!","Das jibbet doch gar nich!","Ach du grüne Neune!","Schon gehört?","Unglaublich!","Ach du dickes Ei!","Ach du liebes bisschen!","Ach, du Schreck!","Da schau her!","Ist nicht wahr!","Oh Gottogott!","Schockschwerenot!","Schreck lass nach!","Guck an!","Teufel auch!","Wahnsinn!");
my $format = '%d.%m.%Y\t%T';
my $period = Time::Piece->strptime($end, $format)
		 - Time::Piece->strptime($begin, $format);
my $percent = $period / 100;
my $strp = DateTime::Format::Strptime->new(
    pattern => '%d.%m.%Y\t%T'
);
my $dt = $strp->parse_datetime($begin);
for (my $var = 1; $var < 101; $var++) {
	my $int = $ints[rand @ints];
	my $p = round($var / 6.6666);
	printf "%s", $dt->add(seconds => $percent)->strftime("%d.%m.%Y\t%T\t");
	my $diff = 15 - $p;
	print "$int\\n";
	print "▓" x $p;
	print "░" x $diff;
	print "\\n$var\% des Semesters sind rum!\n";	
}
