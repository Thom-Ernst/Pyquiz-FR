import pygame

class Track:
    def __init__(self, name, description, song):
        self.name = name
        self.description = description
        self.song = song

    def playsong(self):
        pygame.init()
        music = pygame.mixer.Sound(self.song)
        clock = pygame.time.Clock()
        music.play()
        while True:
            clock.tick(1)