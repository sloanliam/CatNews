import pygame
import file_worker
from pygame.sprite import Sprite


class Cat(Sprite):

    health = 100
    happiness = int(file_worker.load_mood_data())
    hunger_level = int(file_worker.load_food_data())

    def __init__(self, cat_vector, cat_sprite):
        self.cat_vector = cat_vector
        self.cat_sprite = pygame.image.load('assets/cat.png')

    def meow(self):
        pygame.mixer.music.load('assets/Meow-cat-sound-effect.mp3')
        pygame.mixer.music.play(0)

    def draw_cat(self, cat_vector):
        return self.cat_sprite, self.cat_vector
