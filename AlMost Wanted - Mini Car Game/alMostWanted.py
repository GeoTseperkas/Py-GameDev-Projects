import pygame
from pygame.locals import *
import random

# screen
screen = pygame.display.set_mode((1050, 800))
size = width, height = (1050, 800)

# colors
black = (40, 40, 40)
green = (76, 208, 56)
white = (255, 255, 255)

# road
road = width // 1.6
line = width // 80
right_placement = width / 2 + road / 4
left_placement = width / 2 - road / 4
lanes = [left_placement, right_placement]

# difficulty & score counters
dif = 1
dif_counter = 1
score = 1

pygame.init()

running = True
pygame.display.set_caption("AlMost Wanted")

pygame.display.update()

# game logo
sign = pygame.image.load("img/AlMost_Wanted_logo.jpg")
sign_placement = sign.get_rect()
sign_placement.center = width / 4 - road / 4, height * 0.1

# player's car
car = pygame.image.load("img/car.png")
car_placement = car.get_rect()
car_placement.center = right_placement, height * 0.8

# enemy_vehicles
enemy_vehicles = ["img/semi.png", "img/police.png", "img/taxi.png", "img/truck.png", "img/van.png"]
enemy = pygame.image.load("img/police.png")
enemy_placement = enemy.get_rect()
enemy_placement.center = left_placement, height * 0.2

# game loop
while running:
    dif_counter += 1
    if dif_counter == 3000:
        dif += 1
        dif_counter = 0
    enemy_placement[1] += dif
    if enemy_placement[1] > height:
        score += 1
        enemy = pygame.image.load(random.choice(enemy_vehicles))
        enemy_placement.center = lane = random.choice(lanes), -200

    if car_placement[0] == enemy_placement[0] and enemy_placement[1] > car_placement[1] - 200:
        print("Peanut Butter JAIL Time!")
        print("Difficulty level: ", dif)
        print("Score: ", score)
        print()
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT] and car_placement[0] != 233:
                car_placement = car_placement.move([-int(road / 2), 0])
            if event.key in [K_d, K_RIGHT] and car_placement[0] != 561:
                car_placement = car_placement.move([int(road / 2), 0])

    screen.fill(green)
    pygame.draw.rect(screen, black, (width / 2 - road / 2, 0, road, height))
    pygame.draw.rect(screen, white, (width / 2 - line / 2, 0, line, height))
    pygame.draw.rect(screen, white, (width / 2 - road / 2 + line * 2, 0, line, height))
    pygame.draw.rect(screen, white, (width / 2 + road / 2 - line * 3, 0, line, height))

    # display dif
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text_dif = font.render("Difficulty level:  " + str(dif), True, white)
    text_rect_dif = text_dif.get_rect()
    text_rect_dif.center = (80, 200)

    # display score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text_score = font.render("Score:  " + str(score), True, white)
    text_rect_scr = text_score.get_rect()
    text_rect_scr.center = (80, 250)

    screen.blit(car, car_placement)
    screen.blit(enemy, enemy_placement)
    screen.blit(sign, sign_placement)
    screen.blit(text_dif, text_rect_dif)
    screen.blit(text_score, text_rect_scr)
    pygame.display.update()

pygame.quit()