import pygame
from pygame.sprite import Sprite


class Cat(Sprite):

    health = 100
    happiness = 100
    hunger_level = 100

    def __init__(self, cat_vector, cat_sprite):
        self.cat_vector = cat_vector
        self.cat_sprite = pygame.image.load('cat.png')

    def meow(self):
        pygame.mixer.music.load('Meow-cat-sound-effect.mp3')
        pygame.mixer.music.play(0)

    def draw_cat(self, cat_vector):
        return self.cat_sprite, self.cat_vector
