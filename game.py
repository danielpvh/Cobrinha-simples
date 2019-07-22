"""
Script criado por Daniel Cunha em 03 de Julho de 2019
"""

import pygame, constants, sys, state, os, snake, apple, time, inimigo, sound
from pygame.locals import *


from menu import Menu as m



class Game():

    #Inicializa todos os atributos do Jogo. Metodo Construtor
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        try:
            pygame.init()
            constants.RUNNING = True
        except:
            print("Pygame nao foi inicializada corretamente.")

        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

        #Inicializacao dos Objetos
        self.state_game = state.State()
        self.menu = m(self.screen)
        self.snake = snake.Snake(self.screen)
        self.sound = sound.Sound()
        self.time = 0

    #Animacao em producao ainda. Somente para testes.
    def animation(self):

        self.time += 1

        teste = constants.FONT_DEFAULT.render('Teste', False, (constants.WHITE))
        while self.time < 1000:
            self.screen.blit(teste, (80, 80))
            break
        if self.time >= 2000:
            self.time = 0


    def render(self):



        if self.state_game.getState() == 'MENU':
            self.menu.render()
        if self.state_game.getState() == 'LEVEL1':
            self.snake.render()


    def run(self):


        while constants.RUNNING:

            self.render()
            #self.animation()


            for event in pygame.event.get():
                if event.type == QUIT:
                    self.state_game.setstate('QUIT GAME')

                if self.state_game.getState() == 'MENU':
                    if event.type == KEYDOWN:
                        if event.key == K_UP:
                            self.menu.menu_selecao -= 1
                            if  self.menu.menu_selecao < 1:
                                self.menu.menu_selecao = 1
                        if event.key == K_DOWN:
                            self.menu.menu_selecao += 1
                        if self.menu.menu_selecao > 3:
                            self.menu.menu_selecao = 3
                        if self.menu.state == 0:
                            if (event.key == K_RETURN ) and (self.menu.menu_selecao == 1):
                                self.state_game.setstate('LEVEL1')
                            if (event.key == K_RETURN ) and (self.menu.menu_selecao == 2):
                                pass
                            if (event.key == K_RETURN ) and (self.menu.menu_selecao == 3):
                                self.state_game.setstate('QUIT GAME')

                if self.state_game.getState() == 'LEVEL1':

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.state_game.setstate('QUIT GAME')
                        if event.key == K_w:
                            self.snake.my_direction = self.snake.UP
                        if event.key == K_s:
                            self.snake.my_direction = self.snake.DOWN
                        if event.key == K_a:
                            self.snake.my_direction = self.snake.LEFT
                        if event.key == K_d:
                            self.snake.my_direction = self.snake.RIGHT


            pygame.display.update()


game = Game()


game.run()
