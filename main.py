import pygame
import web_worker
import file_worker
from cat import Cat

pygame.init()

screen_x = 500
screen_y = 500

ticks = 0

screen = pygame.display.set_mode([screen_x, screen_y])
pygame.display.set_caption("Cat Game")

cat_x = 175
cat_y = 100

cat1 = Cat(cat_sprite='assets/cat.png', cat_vector=(cat_x, cat_y))

black = (0, 0, 0)
white = (255, 255, 255)

ov_text = ""

exec("web_worker")

clicks = 0

cat1.happiness += web_worker.get_mental_health_data()
cat1.hunger_level -= web_worker.get_food_data()

if cat1.happiness < 0:
    cat1.happiness = 0

if cat1.hunger_level < 0:
    cat1.hunger_level = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicks += 1
            if clicks == 30:
                clicks = 0
            if clicks == 10:
                cat1.meow()
            if cat1.happiness < 100:
                cat1.happiness += 2
            if cat1.happiness == 100:
                cat1.hunger_level += 2

    initial_text_y = 500 - 60
    font = pygame.font.Font('assets/Occams Eraser.ttf', 32)
    con_font = pygame.font.Font('assets/Occams Eraser.ttf', 24)
    health_text = font.render("health " + str(cat1.health), True, black, white)
    happiness_text = font.render("happiness " + str(cat1.happiness), True, black, white)
    hunger_text = font.render("hunger " + str(cat1.hunger_level), True, black, white)
    con_text = con_font.render(ov_text, True, black, white)

    if cat1.hunger_level > 100:
        cat1.hunger_level = 100

    if 80 < cat1.happiness < 100:
        ov_text = "Youre cat is happy!"
    elif 70 < cat1.happiness < 80:
        ov_text = "Youre cat is feeling pretty good"
    elif 60 < cat1.happiness < 70:
        ov_text = "Your cat is alright"
    elif 55 < cat1.happiness < 60:
        ov_text = "Your cat is feeling hopeless"
    elif 40 < cat1.happiness < 55:
        ov_text = "Your cat is very unhappy"
    elif 20 < cat1.happiness < 40:
        ov_text = "Please pet your cat, she is incredibly depressed"
    elif 0 < cat1.happiness < 20:
        ov_text = "Your cat is in bad shape, she needs petting"
    elif cat1.happiness == 0:
        ov_text = "Your cat doesn't want to see humans right now :("

    screen.fill((255, 255, 255))
    screen.blit(cat1.cat_sprite, (cat_x, cat_y))
    screen.blit(con_text, (20, initial_text_y - 36 * 3))
    screen.blit(health_text, (20, initial_text_y))
    screen.blit(happiness_text, (20, initial_text_y - 36))
    screen.blit(hunger_text, (20, initial_text_y - 36 * 2))

    ticks += 1
    if ticks > 100:
        ticks = 0

    pygame.display.flip()

file_worker.write_food_data(str(cat1.hunger_level))
file_worker.write_mood_data(str(cat1.happiness))
pygame.quit()
