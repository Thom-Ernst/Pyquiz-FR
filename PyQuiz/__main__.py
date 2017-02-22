import time
import random
import pygame
from dictionary import chooseListing, chooseTrack
from texts import *
from Layout import Layout
pygame.init()

boolGameloop = True
strNaam = ""
intScore = 0
intRonde = 0

# functions go here


def intro():
    global boolGameloop
    print Layout.bold + textIntro1 + "\n"

    def naamopgeven():
        global strNaam
        strNaam = raw_input(textIntro2 + Layout.blue) + Layout.end
        if strNaam == "":
            print Layout.red + textError1
            naamopgeven()
    naamopgeven()
    print Layout.bold + textIntro3.format(strNaam) + Layout.end


def einde():
    print Layout.bold + textEinde1.format(strNaam, intScore)
    print textEinde2 + Layout.end
    print textEinde3


def startRound():
    print

intro()

while boolGameloop:
    # all the functions executed in their respective order
    chooseListing()
    chooseTrack()
    startRound()

    if intRonde == 10:
        boolGameloop = False

einde()

exit()
