"""Script criado por Daniel Cunha em 16 de Julho e 2019"""


import random, constants, sys
import pygame

lista_inimigos = []


class Inimigo():

    def __init__(self, pname):
        self.name = pname
        self.name_skin = pygame.Surface((10, 10))
        self.name_skin.fill((constants.RED))
        self.pos_x = random.randint(0, constants.SCREEN_WIDTH - 10) // 10 * 10
        self.pos_y = random.randint(0, constants.SCREEN_HEIGHT - 10) // 10 * 10


def criar_inimigo(quant_inimigo):
    for i in range(0, quant_inimigo):
        lista_inimigos.append(Inimigo(i))

def inimigo_render(pscreen):
    for f in range(0, len(lista_inimigos)):
        pscreen.blit(lista_inimigos[f].name_skin, (lista_inimigos[f].pos_y, lista_inimigos[f].pos_x))

