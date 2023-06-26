import pygame
import tkinter as tk
from tkinter import filedialog, simpledialog
import json

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 1000, 563
FPS = 60
WHITE = (255, 255, 255)
background = pygame.image.load("images/bg.jpg")
icon = pygame.image.load("images/space.png")
pygame.mixer.music.load("sounds/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound("sounds/Space_Machine_Power.mp3")
pygame.mixer.Sound.play(sound)

# Configurações da caixa de diálogo
root = tk.Tk()
root.withdraw()

# Criação da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Marker")

# Fonte
font = pygame.font.SysFont(None, 20)

# Dicionário para armazenar as estrelas
estrelas = {}

# Função para desenhar as estrelas e as linhas
def draw():
    background = pygame.image.load("images/bg.jpg")
    icon = pygame.image.load("images/space.png")
    screen.blit(background, (0,0))
    pygame.display.set_icon(icon)
    # Desenha as estrelas
    for nome, pos in estrelas.items():
        pygame.draw.circle(screen, WHITE, pos, 5)
        text = font.render(nome, True, WHITE)
        screen.blit(text, (pos[0] + 10, pos[1] - 10))
    # Desenha as linhas
    for estrela1, pos1 in estrelas.items():
        for estrela2, pos2 in estrelas.items():
            if estrela1 != estrela2:
                distancia = round(((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5)
                pygame.draw.line(screen, WHITE, pos1, pos2)
                text = font.render(str(distancia), True, WHITE)
                screen.blit(text, ((pos1[0] + pos2[0]) // 2, (pos1[1] + pos2[1]) // 2))
    # Desenha os textos adicionais
    text = font.render("Pressione F9 para salvar", True, WHITE)
    screen.blit(text, (10, 10))
    text = font.render("Pressione F10 para carregar", True, WHITE)
    screen.blit(text, (10, 25))
    text = font.render("Pressione F11 para Limpar a tela", True, WHITE)
    screen.blit(text, (10, 40))

    pygame.display.flip()  # Atualiza a tela

# Função para salvar os pontos em um arquivo
def save_points():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            for nome, pos in estrelas.items():
                file.write(f"nome: {nome}, posição: {pos}\n")

# Função para carregar os pontos de um arquivo
def load_points():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        estrelas.clear()  # Limpa o dicionário de estrelas atual
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("nome:"):
                    nome = line.split("nome:")[1].split(",")[0].strip()
                    pos_str = line.split("posição:")[1].strip()
                    pos = tuple(map(int, pos_str.strip("()").split(",")))
                    estrelas[nome] = pos

# Loop principal do programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F9:
                save_points()
            elif event.key == pygame.K_F10:
                load_points()
            elif event.key == pygame.K_F11:
                estrelas.clear()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                nome = tk.simpledialog.askstring("Nome da estrela", "Digite o nome da estrela:")
                if nome is None or nome.strip() == "":
                    nome = "Desconhecido"
                pos = pygame.mouse.get_pos()
                estrelas[nome] = pos

    pygame.display.update()
    
    screen.blit(background, (0,0))


    pygame.display.set_icon(icon)

    draw()

# Salva automaticamente os pontos antes de fechar o programa
save_points()

pygame.quit()