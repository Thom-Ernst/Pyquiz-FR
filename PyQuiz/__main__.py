import time
import pygame
from Track import Track_class
from ConsoleColorsClass import Markup
pygame.init()

firstsong = vivaldi_spring_allegro = Track_class("Lente - Vivaldi", 'music/vivaldi_spring_allegro.ogg')
secondsong = ode_to_joy = Track_class("Ode Aan de Vreugde", 'music/ode_to_joy.ogg')
thirdsong = toccata_and_fugue = Track_class("Toccata en Fugue", 'music/toccata_and_fugue.ogg')
objet1 = True
objet2 = False
objet3 = False

keuze1 = firstsong.name
keuze2 = secondsong.name
keuze3 = thirdsong.name

score = 0


def option1(option, points, song):
    if option is True:
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
    if option is True:
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
    if option is True:
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

# menu = {
#     '1': opt1,
#     '2': opt2,
#     '3': opt3
# }

designated_song = None


def assign_song(chosensong1, chosensong2, chosensong3):
    if chosensong1 is True:
        designated_song = firstsong.song
    elif chosensong2 is True:
        designated_song = secondsong.song
    elif chosensong3 is True:
        designated_song = thirdsong.song
    else:
        print "Error: no song was assigned!"
assign_song(objet1, objet2, objet3)

pygame.mixer.music.load(designated_song)
pygame.mixer.music.play()


def vraag():
    print "De keuzes zijn:"
    print ""
    print "1. {0}".format(keuze1)
    print "2. {0}".format(keuze2)
    print "3. {0}".format(keuze3)
    answer = raw_input("Je antwoord hier: ")
    # menu[answer]()
    if answer is "1":
        pygame.mixer.music.stop()
        option1(objet1, score, thirdsong.song)
    elif answer is "2":
        pygame.mixer.music.stop()
        option2(objet2, score, thirdsong.song)
    elif answer is "3":
        pygame.mixer.music.stop()
        option3(objet3, score, thirdsong.song)
    else:
        print "Je moet een correct getal invoeren!"
        vraag()


print score