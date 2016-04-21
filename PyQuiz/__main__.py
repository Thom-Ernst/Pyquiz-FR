import time
import pygame
from Track import Track_class
from ConsoleColorsClass import Markup
pygame.init()

vivaldi_spring_allegro = Track_class("Lente - Vivaldi", 'music/vivaldi_spring_allegro.ogg')

score = 0

song = "Vivaldi Spring Allegro"


def option1(option, points):
    if option == 1:
        print "Dat is correct!"
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        points += 1
    else:
        print "Dat is niet juist!"
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord is {0}".format(song.name)


def option2(option, points):
    if option == 1:
        print "Dat is correct!"
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        points += 1
    else:
        print "Dat is niet juist!"
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord is {0}".format(song.name)


def option3(option, points):
    if option == 1:
        print "Dat is correct!"
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        points += 1
    else:
        print "Dat is niet juist!"
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord is {0}".format(song.name)

menu = {
    '1': option1,
    '2': option2,
    '3': option3
}

pygame.mixer.music.load('music/vivaldi_spring_allegro.ogg')
pygame.mixer.music.play()
print "De keuzes zijn:"
print ""
print "1. {0}".format(keuze1)
print "2. {0}".format(keuze2)
print "3. {0}".format(keuze3)
raw_input("Je antwoord hier: ")