#! /usr/bin/env/python

from datetime import datetime, timedelta
import random

############################################################################
# A script to create tweets for a progress bar bot
# Made by Simon Meier-Vieracker, @fussballinguist, www.fussballlinguistik.de
############################################################################

# --> Adjust the beginning and end of the semester
begin = '11.10.2021\t07:30:00'
end = '04.02.2022\t20:00:00'

#############################
# No changes below this line!
#############################

interjections = ["\\\\o\/","Mein lieber Herr Gesangsverein!","Scheiß die Wand an!","Alter Schwede!","Heidewitzka!","Holla die Waldfee!","WTF!!","Ach du grüne Neune!","Sapperlot!","Ich glaub, mein Schwein pfeift!","Heiliger Bimbam!","Prost Mahlzeit!","Da brat mir einer n Storch!","Ach du meine Nase!","Hör mir auf!","Mannometer!","Ist es zu glauben?","Oh my fucking goodness!","Lecko mio!","Alter!","Gopferdeggl!","Grundgütiger!","Krass!","Juhuu!","Echt jetzt?","Tschakka!","Derbst, Alter!","Gimme five!","Da legst di nieda!","Eieiei!","Heiliger Strohsack!","Dat jibbet doch gar nich!","Ach du grüne Neune!","Schon gehört?","Unglaublich!","Ach du dickes Ei!","Ach du liebes bisschen!","Ach, du Schreck!","Da schau her!","Ist nicht wahr!","Oh Gottogott!","Schockschwerenot!","Schreck lass nach!","Guck an!","Teufel auch!","Wahnsinn!","Oje, ojemine!","Ich werd verrückt!","Da wird doch der Hund in der Pfanne verrückt!","Allmecht!","Oha!","Ich glaub mich laust der Affe!","Ich glaub, mich knutscht ein Elch!","Zum Donnerkeil!","Ich glaub, mein Hamster bohnert!","Meine Fresse!","Alter Falter!","Menschenskinder!","Ach du liebes Lieschen!","Ach du liebe Zeit!","Donnerlittchen!","Jesses, Maria und Joseph!","Heiliger Bimbam!","Heidewitzka!","Ich krieg die Motten!","Ich glaub, mich tritt ein Pferd!","Potz Blitz!"]

fmt = '%d.%m.%Y\t%X'
period = datetime.strptime(end, fmt) - datetime.strptime(begin, fmt)
percent = period.total_seconds() / 100

dt = datetime.strptime(begin, fmt)

for i in range(1,101):
	p = round(i / (100 / 15))
	diff = 15 - p
	interjection = random.choice(interjections)
	dt += timedelta(seconds=percent)
	print(f'{dt.strftime(fmt)}\t{interjection}\\n{p * "▓"}{diff * "░"}', end='')
	print(f'\\n{i}% des Semesters sind rum.')
