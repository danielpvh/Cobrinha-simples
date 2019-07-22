"""
Script criado por Daniel Cunha em 5 de Julho sw 2019
"""

import pygame, os, random, inimigo, snake, state
import  constants as c



class Apple():

    def __init__(self):



        self.apple = pygame.Surface((10, 10))
        self.apple.fill(c.GREEN)
        self.apple_pos = self.on_grid_random()

        self.apple_blue = pygame.Surface((10, 10))
        self.apple_blue.fill(c.BLUE)
        self.apple_blue_pos = self.on_grid_random()
        self.apple_blue_last_pos = []
        self.apple_blue_time_render = 0
        self.label_bonus_time = 0
        self.mostra_bonus_switch = False
        self.inimigo_red_time = 0
        self.colission = False


    def on_grid_random(self):
        x = random.randint(10, 670)
        y = random.randint(0, 450)
        return (x // 10 * 10, y // 10 * 10)


    def render(self, screen):

        self.apple_blue_time_render += 1
        self.inimigo_red_time += 1
        if self.mostra_bonus_switch:
            self.label_bonus_time += 1
            if self.label_bonus_time == 30:
                self.label_bonus_time = 0
                self.mostra_bonus_switch = False

        screen.blit(self.apple, self.apple_pos)
        self.apple_blue23(screen)
        self.inimigo_red_render(screen)
        self.mostra_bonus(screen)



    def apple_blue23(self, screen):

        #Enquanto for verdadeiro ira renderizar na tela. Isso cria um time para a apple_blue ficar renderizada
        #na tela do usuario
        while (self.apple_blue_time_render > 300) and (self.apple_blue_time_render < 500):
            screen.blit(self.apple_blue, self.apple_blue_pos)
            break

        #Reinicia o apple_blue_time_render para 0 para recomencar o ciclo de novo
        if self.apple_blue_time_render == 1000:
            self.apple_blue_time_render = 0

    def inimigo_red_render(self, screen):
        while (self.inimigo_red_time > 500) and (self.inimigo_red_time < 1000):
            inimigo.inimigo_render(screen)
            break


        if self.inimigo_red_time == 2000:
            #Gera um numero aleatorio de inimigos na tela
            inimigo.criar_inimigo(random.randint(0, 90))
        #Reinicia o contador
        if self.inimigo_red_time > 2000:
            self.inimigo_red_time = 0

        if (self.inimigo_red_time > 500) and (self.inimigo_red_time < 1000):
            self.colission = True
        else:
            self.colission = False

    def mostra_bonus(self, screen):

        while self.label_bonus_time > 2 and self.label_bonus_time < 30:
            layout = c.FONT_DEFAULT.render('+500', True, c.YELLOW)
            screen.blit(layout, (self.apple_blue_last_pos[0], self.apple_blue_last_pos[1]-20))
            break