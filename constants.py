"""
Criado por Daniel Cunha em 03 de Julho de 2019

Modulo referente a constantes do jogo
"""

import pygame

pygame.font.init()

RUNNING = False
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 460
FONT_DEFAULT = pygame.font.SysFont('Arial', 30)

#Menu
NOVO_JOGO = 'Novo Jogo'
CREDITOS = 'Creditos'
SAIR = 'Sair'
CURSOR_MENU = '>>'
TELA_CREDITOS = 'Criado por Daniel Cunha Versao 1.0'
TELA_CREDITOS_VOLTAR = 'Voltar'

#Cores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)