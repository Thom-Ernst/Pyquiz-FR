import pygame

class Track_class:
    def __init__(self, name, song):
        self.name = name
        self.song = song

    def playsong(self):
        pygame.init()
        music = pygame.mixer.Sound(self.song)
        clock = pygame.time.Clock()
        music.play()
        while True:
            clock.tick(1)