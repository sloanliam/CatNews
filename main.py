import pygame
from cat import Cat
pygame.init()

screen_x = 500
screen_y = 500

ticks = 0

screen = pygame.display.set_mode([screen_x, screen_y])
pygame.display.set_caption("Cat Game")

cat_x = 175
cat_y = 100

cat1 = Cat(cat_sprite='cat.png', cat_vector=(cat_x, cat_y))

black = (0, 0, 0)
white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            cat1.meow()
            if cat1.happiness < 100:
                cat1.happiness += 1

    initial_text_y = 500 - 60
    font = pygame.font.Font('Occams Eraser.ttf', 32)
    health_text = font.render("health " + str(cat1.health), True, black, white)
    happiness_text = font.render("happiness " + str(cat1.happiness), True, black, white)
    hunger_text = font.render("hunger " + str(cat1.hunger_level), True, black, white)

    screen.fill((255, 255, 255))
    screen.blit(cat1.cat_sprite, (cat_x, cat_y))
    screen.blit(health_text, (20, initial_text_y))
    screen.blit(happiness_text, (20, initial_text_y - 36))
    screen.blit(hunger_text, (20, initial_text_y - 36 * 2))

    ticks += 1
    if ticks > 100:
        ticks = 0

    pygame.display.flip()

pygame.quit()
