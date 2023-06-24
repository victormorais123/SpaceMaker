#main imports
import pygame 
from tkinter import simpledialog
import random
import os

#main vars
pygame.init()
running = True
length = (800, 563)
background = pygame.image.load("images/bg.jpg")
icon = pygame.image.load("images/space.png")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(length) #moving the screen to the middle

pygame.mixer.music.load("sounds/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound("sounds/Space_Machine_Power.mp3")
#pygame.mixer.Sound.play(sound)
estrelas = {'Nome': 'Posicao'}
#main
running = True
while running:
    for event in pygame.event.get(): #func get captures all the events that happen on keyboard, moouse, etc
        if event.type == pygame.QUIT:
            running = False  
        elif running == True:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                item = simpledialog.askstring("Space", "Nome da Estrela:")
                print(item)
                if item == None:
                    item = "desconhecido"+str(pos)
                estrelas[item] = pos
                print(estrelas)
                pygame.draw.circle(screen, (255,255,255), pos, 5)
                

    pygame.display.update()
    screen.blit(background, (0,0))

    pygame.display.set_icon(icon)

    clock.tick(60)

pygame.quit()   
