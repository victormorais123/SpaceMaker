#main imports
import pygame 
from tkinter import simpledialog
from func import *


#main vars
pygame.init()
running = True
length = (1000, 563)
background = pygame.image.load("images/bg.jpg")
icon = pygame.image.load("images/space.png")
clock = pygame.time.Clock()
screen = pygame.display.set_mode(length) #moving the screen to the middle

pygame.mixer.music.load("sounds/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound("sounds/Space_Machine_Power.mp3")
pygame.mixer.Sound.play(sound)

estrelas = {"nome": 'Pos'}

def show_dialog(pos):
    nome = simpledialog.askstring("Space", "Nome da Estrela:")
    if nome is None or nome.strip() == "":
        nome = "Desconhecido"
    estrelas[nome] = pos

def draw_star(pos, nome):
    pygame.draw.circle(screen, (255, 255, 255), pos, 5)
    fonte = pygame.font.Font(None, 20)
    texto = fonte.render(nome, True, (255, 255, 255))
    largura_texto = texto.get_width()
    altura_texto = texto.get_height()
    pos_texto = (round(pos[0] - largura_texto / 2), round(pos[1] - altura_texto / 2))
    screen.blit(texto, pos_texto)


def draw_lines():
    pontos = list(estrelas.values())
    if len(pontos) >= 2:
        pygame.draw.lines(screen, (255, 255, 255), False, pontos, 2)


def save_stars():
    archive = open("stars.txt", "w")
    for nome, pos in estrelas.items():
        linha = f"nome: {nome}, posição: {pos} \n"
        archive.write(linha)
    archive.close()


fonte_texto = pygame.font.Font(None, 20)
texto_salvar = fonte_texto.render("Pressione F9 para salvar", True, (255, 255, 255))
pos_texto_salvar = (10, 10)


# opção de carregamento
texto_carregar = fonte_texto.render("Pressione F10 para carregar", True, (255, 255, 255))
pos_texto_carregar = texto_carregar.get_rect(topleft=(10, 25))


# limpar tela
texto_limpar_tela = fonte_texto.render("Pressione F11 para Limpar a tela", True, (255, 255, 255))
pos_texto_limpar_tela = texto_limpar_tela.get_rect(topleft=(10, 40))


#main
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                show_dialog(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F9:
                save_stars()


    for nome, pos in estrelas.items():
        draw_star((pos, pos), nome)
   
    draw_lines()


    screen.blit(texto_salvar, pos_texto_salvar)
    screen.blit(texto_carregar, pos_texto_carregar)
    screen.blit(texto_limpar_tela, pos_texto_limpar_tela)
       
    pygame.display.update()


    screen.blit(background, (0,0))


    pygame.display.set_icon(icon)


    clock.tick(60)
   
pygame.quit()

