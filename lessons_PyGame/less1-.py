import pygame
import pygame as pg


SCREEN_WEIGHT = 720
SCREEN_HIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WEIGHT, SCREEN_HIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


