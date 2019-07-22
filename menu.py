"""
Criado por Daniel Cunha em 3 de Julho de 2019
"""

import constants as c
import os, pygame, sound

class Menu():

    def __init__(self, pscreen):
        self.screen = pscreen
        self.state = 0
        self.fonte_menu = c.FONT_DEFAULT
        self.menu_selecao = 1

    def render(self):


        if self.state == 0:

            if self.menu_selecao == 1:
                self.screen.fill((c.BLACK))
                #Renderiza NOVO JOGO
                novo_jogo_render = self.fonte_menu.render(c.NOVO_JOGO, True, (c.WHITE))
                cursor_render = self.fonte_menu.render(c.CURSOR_MENU, True, (c.WHITE))
                self.screen.blit(novo_jogo_render,((c.SCREEN_WIDTH/2) - novo_jogo_render.get_width()/2, c.SCREEN_HEIGHT/2))
                self.screen.blit(cursor_render,((c.SCREEN_WIDTH / 2) - 100, c.SCREEN_HEIGHT / 2))


                #Renderiza Creditos
                creditos_render = self.fonte_menu.render(c.CREDITOS, True, (c.WHITE))
                self.screen.blit(creditos_render, ((c.SCREEN_WIDTH/2)- (creditos_render.get_width()/2), c.SCREEN_HEIGHT / 2 + 30))

                #Renderiza SAIR
                sair_render = self.fonte_menu.render(c.SAIR, True, (c.WHITE))
                self.screen.blit(sair_render,((c.SCREEN_WIDTH / 2) - (sair_render.get_width() / 2), c.SCREEN_HEIGHT / 2 + 60))

            elif self.menu_selecao == 2:
                self.screen.fill((c.BLACK))
                #Renderiza NOVO JOGO
                novo_jogo_render = self.fonte_menu.render(c.NOVO_JOGO, True, (c.WHITE))
                cursor_render = self.fonte_menu.render(c.CURSOR_MENU, True, (c.WHITE))
                self.screen.blit(novo_jogo_render,((c.SCREEN_WIDTH/2) - novo_jogo_render.get_width()/2, c.SCREEN_HEIGHT/2))
                #self.screen.blit(cursor_render,((c.SCREEN_WIDTH / 2) - 100, c.SCREEN_HEIGHT / 2))


                #Renderiza Creditos
                creditos_render = self.fonte_menu.render(c.CREDITOS, True, (c.WHITE))
                self.screen.blit(creditos_render, ((c.SCREEN_WIDTH/2)- (creditos_render.get_width()/2), c.SCREEN_HEIGHT / 2 + 30))
                self.screen.blit(cursor_render, ((c.SCREEN_WIDTH / 2) - 100, (c.SCREEN_HEIGHT / 2)+ 30))


                #Renderiza SAIR
                sair_render = self.fonte_menu.render(c.SAIR, True, (c.WHITE))
                self.screen.blit(sair_render,((c.SCREEN_WIDTH / 2) - (sair_render.get_width() / 2), c.SCREEN_HEIGHT / 2 + 60))

            elif self.menu_selecao == 3:
                self.screen.fill((c.BLACK))
                #Renderiza NOVO JOGO
                novo_jogo_render = self.fonte_menu.render(c.NOVO_JOGO, True, (c.WHITE))
                cursor_render = self.fonte_menu.render(c.CURSOR_MENU, True, (c.WHITE))
                self.screen.blit(novo_jogo_render,((c.SCREEN_WIDTH/2) - novo_jogo_render.get_width()/2, c.SCREEN_HEIGHT/2))
                #self.screen.blit(cursor_render,((c.SCREEN_WIDTH / 2) - 100, c.SCREEN_HEIGHT / 2))


                #Renderiza Creditos
                creditos_render = self.fonte_menu.render(c.CREDITOS, True, (c.WHITE))
                self.screen.blit(creditos_render, ((c.SCREEN_WIDTH/2)- (creditos_render.get_width()/2), c.SCREEN_HEIGHT / 2 + 30))
                #self.screen.blit(cursor_render, ((c.SCREEN_WIDTH / 2) - 100, (c.SCREEN_HEIGHT / 2)+ 30))


                #Renderiza SAIR
                sair_render = self.fonte_menu.render(c.SAIR, True, (c.WHITE))
                self.screen.blit(sair_render,((c.SCREEN_WIDTH / 2) - (sair_render.get_width() / 2), c.SCREEN_HEIGHT / 2 + 60))
                self.screen.blit(cursor_render, ((c.SCREEN_WIDTH / 2) - 100, (c.SCREEN_HEIGHT / 2) + 60))

        #Exibe a Tela de Creditos
        elif self.state == 1:

            self.screen.fill(c.BLACK)
            creditos = self.fonte_menu.render(c.TELA_CREDITOS, True, (c.WHITE))
            voltar = self.fonte_menu.render(c.TELA_CREDITOS_VOLTAR, True, (c.WHITE))
            cursor_render = self.fonte_menu.render(c.CURSOR_MENU, True, (c.WHITE))
            self.screen.blit(creditos,((c.SCREEN_WIDTH/2) - creditos.get_width()/2, (c.SCREEN_HEIGHT/2)- creditos.get_height()/2))
            self.screen.blit(voltar, ((c.SCREEN_WIDTH/2) - voltar.get_width()/2, c.SCREEN_HEIGHT - 50))
            self.screen.blit(cursor_render, ((c.SCREEN_WIDTH / 2) - (voltar.get_width() / 2) - 40, c.SCREEN_HEIGHT - 50))

    def control(self):
        pass