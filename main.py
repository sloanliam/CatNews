import pygame

import cat
from cat import Cat
pygame.init()

screen_x = 500
screen_y = 500

screen = pygame.display.set_mode([screen_x, screen_y])
pygame.display.set_caption("Cat Game")

cat1 = Cat(cat_sprite='cat.png', cat_vector=(175, 100))

black = (0, 0, 0)
white = (255, 255, 255)

initial_text_y = 500 - 60
font = pygame.font.Font('Occams Eraser.ttf', 32)
health_text = font.render("health " + str(cat1.health), True, black, white)
happiness_text = font.render("happiness " + str(cat1.happiness), True, black, white)
hunger_text = font.render("hunger " + str(cat1.hunger_level), True, black, white)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            cat1.meow()

    screen.fill((255, 255, 255))
    screen.blit(cat1.cat_sprite, cat1.cat_vector)
    screen.blit(health_text, (20, initial_text_y))
    screen.blit(happiness_text, (20, initial_text_y - 36))
    screen.blit(hunger_text, (20, initial_text_y - 36 * 2))

    pygame.display.flip()

pygame.quit()
