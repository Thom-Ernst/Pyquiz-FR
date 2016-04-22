import time
from ConsoleColorsClass import *

score = 0

print Markup.green + Markup.bold + "Hallo, welkom bij PyQuiz!" + Markup.end
time.sleep(1)
print Markup.green + "Tijd om liedjes te raden!" + Markup.end
time.sleep(1)

naam = raw_input(Markup.red + "Maar eerst: Wat is je naam? (typ je naam en druk op enter) "+ Markup.end)
print Markup.green + "Laten we beginnen, {0}.".format(naam) + Markup.end
time.sleep(0.5)
raw_input(Markup.green + "Druk op die enter knop, en dan kunnen we beginnen!" + Markup.end)

print "\n" * 90