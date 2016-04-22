import time
from ConsoleColorsClass import *

naam = "Kathleen"
score = 0

print "\n" * 90

print Markup.green + "Het spel is voorbij!" + Markup.end
time.sleep(0.5)
print Markup.green + "Thom en Kathleen danken je voor het spelen!" + Markup.end
time.sleep(0.5)
print Markup.red + "Je score was {0}!".format(score) + Markup.end
time.sleep(1)
print Markup.green + Markup.bold + "Kom nog maar eens terug, {0}".format(naam) + Markup.end

print "\n" * 4
raw_input("Druk op enter om te eindigen.")

