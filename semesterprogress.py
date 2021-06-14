from datetime import datetime, timedelta
import random

begin = '12.04.2021\t07:30:00'
end = '23.07.2021\t20:00:00'

interjections = ["\\\\o\/","Mein lieber Herr Gesangsverein!","Scheiß die Wand an!","Alter Schwede!","Heidewitzka!","Holla die Waldfee!","WTF!!","Ach du grüne Neune!","Sapperlot!","Ich glaub, mein Schwein pfeift!","Heiliger Bimbam!","Prost Mahlzeit!","Da brat mir einer n Storch!","Ach du meine Nase!","Hör mir auf!","Mannometer!","Ist es zu glauben?","Oh my fucking goodness!","Lecko mio!","Alter!","Gopferdeggl!","Grundgütiger!","Krass!","Juhuu!","Echt jetzt?","Tschakka!","Derbst, Alter!","Gimme five!","Da legst di nieda!","Eieiei!","Heiliger Strohsack!","Dat jibbet doch gar nich!","Ach du grüne Neune!","Schon gehört?","Unglaublich!","Ach du dickes Ei!","Ach du liebes bisschen!","Ach, du Schreck!","Da schau her!","Ist nicht wahr!","Oh Gottogott!","Schockschwerenot!","Schreck lass nach!","Guck an!","Teufel auch!","Wahnsinn!"]

fmt = '%d.%m.%Y\t%X'
period = datetime.strptime(end, fmt) - datetime.strptime(begin, fmt)
percent = period.total_seconds() / 100

dt = datetime.strptime(begin, fmt)

for i in range(1,101):
	p = round(i / (100 / 15))
	diff = 15 - p
	interjection = random.choice(interjections)
	dt += timedelta(seconds=percent)
	print(f'{dt}\t{interjection}\\n{p * "▓"}{diff * "░"}', end='')
	print(f'\\n{i}% des Semesters sind rum.')
