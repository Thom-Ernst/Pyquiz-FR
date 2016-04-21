import time
import pygame
from Track import Track_class
from ConsoleColorsClass import Markup
pygame.init()

firstsong = vivaldi_spring_allegro = Track_class("Lente - Vivaldi", 'music/vivaldi_spring_allegro.ogg')
secondsong = ode_to_joy = Track_class("Ode Aan de Vreugde", 'music/ode_to_joy.ogg')
thirdsong = toccata_and_fugue = Track_class("Toccata en Fugue", 'music/toccata_and_fugue.ogg')
objet1 = 1
objet2 = 0
objet3 = 0

keuze1 = firstsong.name
keuze2 = secondsong.name
keuze3 = thirdsong.name

score = 0


def option1(option, points, song):
    if option == 1:
        print "Dat is correct!"
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        points += 1
    else:
        print "Dat is niet juist!"
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord was {0}".format(song.name)


def option2(option, points, song):
    if option == 1:
        print "Dat is correct!"
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        points += 1
    else:
        print "Dat is niet juist!"
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord was {0}".format(song.name)


def option3(option, points, song):
    if option == 1:
        print "Dat is correct!"
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        points += 1
    else:
        print "Dat is niet juist!"
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord was {0}".format(song.name)


# menu = {
#     '1': option1(objet1, score, keuze1),
#     '2': option2(objet2, score, keuze2),
#     '3': option3(objet3, score, keuze3)
# }


def opt1():
    pygame.mixer.music.stop()
    option1(objet1, score, keuze1)


def opt2():
    pygame.mixer.music.stop()
    option2(objet2, score, keuze2)


def opt3():
    pygame.mixer.music.stop()
    option3(objet3, score, keuze3)

menu = {
    '1': opt1,
    '2': opt2,
    '3': opt3
}

designated_song = firstsong.song
if objet1 == 1:
    designated_song = firstsong.song
elif objet2 == 1:
    designated_song = secondsong.song
elif objet3 == 1:
    designated_song = thirdsong.song
else:
    print "Error: no song was assigned!"

pygame.mixer.music.load(designated_song)
pygame.mixer.music.play()
print "De keuzes zijn:"
print ""
print "1. {0}".format(keuze1)
print "2. {0}".format(keuze2)
print "3. {0}".format(keuze3)
answer = raw_input("Je antwoord hier: ")
menu[answer]()
print score