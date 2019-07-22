"""
Criado por Daniel Cunha em 3 de Julho de 2019
"""

import pygame, sys

class State():

    def __init__(self):

        self.last_state = 0
        self.current_state = 'MENU'


    def getState(self):
        return self.current_state

    def setstate(self, pstate):
        self.last_state = self.current_state
        self.current_state = pstate
        self.state_control()

    def state_control(self):

        if self.current_state == 'QUIT GAME':
            pygame.quit()
            sys.exit()