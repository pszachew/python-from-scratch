import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((800, 600))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                window.fill((24, 164, 240))
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                window.fill((10, 1, 120))
                pygame.display.update()
            if event.key == pygame.K_UP:
                left = randint(1, 800)
                right = randint(1, 400)
                pygame.draw.rect(window, (255, 0, 0), pygame.Rect(left, right, 10, 15))
                pygame.display.update()
