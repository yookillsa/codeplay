# -*- coding: utf-8 -*-
import pygame 

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()


while True: 
    screen.fill((0,0,0))

    event = pygame.event.poil()
    if event.type == pygame.QUIT:
        break

    pygame.display.update()
    clock.tick(30)


pygame.Quit()