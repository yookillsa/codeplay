# -*- coding: utf-8 -*-ㅌㅋ
import pygame
pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("똥피하기 - 코드플레이")
bg = pygame.image.load("pygame/source/bg.png")


running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("죽여줘!!!")
            running = False



    screen.blit(bg,(0, 0))
    pygame.display.update()


pygame.quit()     






