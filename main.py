#main imports

import pygame 
from tkinter import simpledialog
import random
import os

#main vars
pygame.init()
length = (800, 600)
background = pygame.image.load("images/space.png")
#icon = pygame.image.load("images/space.ico")
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(length) #moving the screen to the middle


#main
running = True
while running:
    for event in pygame.event.get(): #func get captures all the events that happen on keyboard, moouse, etc
        if event.type == pygame.QUIT:
            running = False
            screen.blit(background, (0,0))
            
    pygame.display.update()
    clock.tick(60)
pygame.quit()   
