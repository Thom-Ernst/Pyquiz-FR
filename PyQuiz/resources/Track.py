import pygame

class Track:
    def __init__(self, name, description, song):
        self.name = name
        self.description = description
        self.song = song
        music = pygame.mixer.Sound(song)

    def playsong(self):
        pygame.init()
        music = pygame.mixer.Sound(self.song)