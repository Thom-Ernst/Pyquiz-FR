import time
import pygame
import random
from randomiser import *
from ConsoleColorsClass import Markup
pygame.init()

game = True
counter = 0
score = 0
ronde = 1
naam = ""

def reset_game():
    counter = 0
    score = 0
    ronde = 1
    naam = ""
    game = True

while game:
    counter += 1
    if counter == 10:
        game = False

    def generatesongs():
        global firstsong
        global secondsong
        global thirdsong
        firstsong = random.choice(songs_array)
        secondsong = random.choice(songs_array)
        thirdsong = random.choice(songs_array)

    generatesongs()

    true_false = [False, True, False, True, False, False, True, False, False]
    objet1 = random.choice(true_false)
    objet2 = random.choice(true_false)
    objet3 = random.choice(true_false)
    if objet1 is True:
        objet2 == False
        objet3 == False
    elif objet2 is True:
        objet1 == False
        objet3 == False
    elif objet3 is True:
        objet1 == False
        objet2 == False
    else:
        objet1 = True

    keuze1 = firstsong.name
    keuze2 = secondsong.name
    keuze3 = thirdsong.name


    def intro():
        global naam
        pygame.mixer.music.load('music/intro.ogg')
        pygame.mixer.music.play(1)
        time.sleep(3)
        print Markup.green + Markup.bold + "Hallo, welkom bij PyQuiz!" + Markup.end
        time.sleep(1)
        print Markup.green + "Tijd om liedjes te raden!" + Markup.end
        time.sleep(1)
        naam = raw_input(Markup.red + "Maar eerst: Wat is je naam? (typ je naam en druk op enter) "+ Markup.end)
        print Markup.green + "Laten we beginnen, {0}.".format(naam) + Markup.end
        time.sleep(0.5)
        raw_input(Markup.green + "Druk op die enter knop, en dan kunnen we beginnen!" + Markup.end)
        print "\n" * 90

        begin_ronde()

    def option1(option):
        global score
        if option is True:
            print Markup.green + "Dat is correct!" + Markup.end
            pygame.mixer.music.load('sounds/Nyes.ogg')
            pygame.mixer.music.play()
            time.sleep(3)
            score += 1
        else:
            print Markup.red + "Dat is niet juist!" + Markup.end
            pygame.mixer.music.load('sounds/No.ogg')
            pygame.mixer.music.play()
            time.sleep(1)
            raw_input("Druk op Enter om door te gaan... ")


    def option2(option):
        global score
        if option is True:
            print Markup.green + "Dat is correct!" + Markup.end
            pygame.mixer.music.load('sounds/Nyes.ogg')
            pygame.mixer.music.play()
            time.sleep(3)
            score += 1
        else:
            print Markup.red + "Dat is niet juist!" + Markup.end
            pygame.mixer.music.load('sounds/No.ogg')
            pygame.mixer.music.play()
            time.sleep(1)
            raw_input("Druk op Enter om door te gaan... ")


    def option3(option):
        global score
        if option is True:
            print Markup.green + "Dat is correct!" + Markup.end
            pygame.mixer.music.load('sounds/Nyes.ogg')
            pygame.mixer.music.play()
            time.sleep(3)
            score += 1
        else:
            print Markup.red + "Dat is niet juist!" + Markup.end
            pygame.mixer.music.load('sounds/No.ogg')
            pygame.mixer.music.play()
            time.sleep(1)
            raw_input("Druk op Enter om door te gaan... ")


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
            option1(objet1)
        elif answer == "2":
            pygame.mixer.music.stop()
            option2(objet2)
        elif answer == "3":
            pygame.mixer.music.stop()
            option3(objet3)
        else:
            print "Je moet een correct getal invoeren!"
            vraag()


    def begin_ronde():
        global ronde
        global vraag
        pygame.mixer.music.stop()
        time.sleep(0.5)
        print "Ronde {0}...".format(ronde)
        ronde += 1
        designated_song.playsong()
        vraag()

    if counter < 2:
        global intro
        intro()

    begin_ronde()

    if score == 1:
        print "Je hebt nu {0} punt!".format(score)
    else:
        print "Je hebt nu {0} punten!".format(score)
    time.sleep(2)
    print "\n" * 30


if game is False:
    time.sleep(1)
    print "Dit was het einde van het spel!"
    time.sleep(0.5)
    print "Bedankt om mee te spelen!"
    time.sleep(0.5)
    print "Je hebt een score van {0} behaald!".format(score)
    if score < 5:
        time.sleep(0.5)
        print "Volgende keer misschien beter!"
    else:
        time.sleep(0.5)
        print "Goed werk!!"
    time.sleep(1.5)
    print "\n"
    print "Dit spel werd voor u gemaakt door Thom Ernst en Kathleen Puvrez."
    time.sleep(0.2)
    print Markup.green + Markup.bold + "Kom nog maar eens terug, {0}".format(naam) + Markup.end
    time.sleep(5)
    raw_input("Druk op de entertoets om het spel opnieuw op te starten... ")
    print "\n" * 50
    reset_game()
