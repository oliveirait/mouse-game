import random
import pygame
from pygame.locals import *
from sys import exit
from values.var import *

def posicao_elemento() -> list:
    pos1 = random.randint(1,720)
    pos2 = random.randint(1,720)
    pos = [pos1, pos2]
    return pos

def tela_pos_win():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
                exit(0)
            screen.fill((azul))
            screen.blit(text, textRect)
            pygame.display.update()

pygame.init()

# DEFINICAO DE FONTES E CORES
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Parabens, você venceu!', True, verde, azul)
textRect = text.get_rect()
textRect.center = (pos_x // 2, pos_y // 2)

# INSTANCIA QUE DEFINE O TAMANHO DA TELA
screen = pygame.display.set_mode((pos_x, pos_y))

# DEFINE O TITULO DA JANELA
pygame.display.set_caption('Joguinho do mouse')

# VARIAVEL RECEBE O RETORNO DA FUNCAO COM A POSICAO DO ELEMENTO NA TELA
posicao_pontinho = posicao_elemento()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            exit(0)

    for event in pygame.event.get():
        posicao_mouse = list(pygame.mouse.get_pos())

        if posicao_mouse == posicao_pontinho:
            pontos += 1
            posicao_pontinho = posicao_elemento()

        if pontos == 5:
            tela_pos_win()
            
        else:
            screen.fill((vermelho))
            pygame.draw.rect(screen, (branco), [posicao_pontinho[0], posicao_pontinho[1],altura,largura])
            pygame.display.update()
        