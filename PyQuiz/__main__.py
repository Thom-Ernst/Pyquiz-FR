import time
import pygame
from randomiser import *
from dictionary import *
from Track import Track_class
from ConsoleColorsClass import Markup
pygame.init()

generatesongs()

objet1 = False
objet2 = False
objet3 = True

keuze1 = firstsong.name
keuze2 = secondsong.name
keuze3 = thirdsong.name

score = 0
ronde = 1


def option1(option, song):
    global score
    if option is True:
        print Markup.green + "Dat is correct!" + Markup.end
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        score += 1
    else:
        print Markup.red + "Dat is niet juist!" + Markup.end
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord was {0}".format(song.name)


def option2(option, song):
    global score
    if option is True:
        print Markup.green + "Dat is correct!" + Markup.end
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        score += 1
    else:
        print Markup.red + "Dat is niet juist!" + Markup.end
        pygame.mixer.music.load('sounds/No.ogg')
        pygame.mixer.music.play()
        print "Het juiste antwoord was {0}".format(song.name)


def option3(option, song):
    global score
    if option is True:
        print Markup.green + "Dat is correct!" + Markup.end
        pygame.mixer.music.load('sounds/Nyes.ogg')
        pygame.mixer.music.play()
        score += 1
    else:
        print Markup.red + "Dat is niet juist!" + Markup.end
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
if objet1 is True:
    designated_song = firstsong
elif objet2 is True:
    designated_song = secondsong
elif objet3 is True:
    designated_song = thirdsong
else:
    print "Error: no song was assigned!"


def vraag():
    print "De keuzes zijn:"
    print ""
    time.sleep(1)
    print Markup.blue + "1. {0}".format(keuze1) + Markup.end
    time.sleep(0.5)
    print Markup.blue + "2. {0}".format(keuze2) + Markup.end
    time.sleep(0.5)
    print Markup.blue + "3. {0}".format(keuze3) + Markup.end
    answer = raw_input(Markup.purple + "Typ antwoord hier:  " + Markup.end)
    # menu[answer]()
    if answer == "1":
        pygame.mixer.music.stop()
        option1(objet1, firstsong.song)
    elif answer == "2":
        pygame.mixer.music.stop()
        option2(objet2, secondsong.song)
    elif answer == "3":
        pygame.mixer.music.stop()
        option3(objet3, thirdsong.song)
    else:
        print "Je moet een correct getal invoeren!"
        vraag()


def begin_ronde():
    global ronde
    global vraag
    print "Ronde {0}...".format(ronde)
    ronde += 1
    designated_song.playsong()
    vraag()

begin_ronde()

print "Je hebt nu {0} punten!".format(score)