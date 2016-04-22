from dictionary import *
import random

songs_array = [
    songs['rock1'],
    songs['rock2'],
    songs['rock3'],
    songs['pop1'],
    songs['pop2'],
    songs['pop3'],
    songs['90s2'],
    songs['90s1'],
    songs['90s3'],
    songs['00s1'],
    songs['00s2'],
    songs['00s3'],
    songs['reggea1'],
    songs['reggea2'],
    songs['reggea3'],
    songs['80s1'],
    songs['80s2'],
    songs['80s3'],
    songs['jazz1'],
    songs['jazz2'],
    songs['jazz3'],
    songs['klassiek1'],
    songs['klassiek2'],
    songs['klassiek3'],
    songs['meme1'],
    songs['meme2'],
    songs['meme3'],
]
def generatesongs():
    firstsong = random.choice(songs_array)
    secondsong = random.choice(songs_array)
    thirdsong = random.choice(songs_array)

