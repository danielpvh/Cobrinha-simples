"""
Script criado por Daniel Cunha em 21 de Julho de 2019
"""

import os, pygame

class Sound():

    def __init__(self):
        #Pega o caminho dos audio
        #self.coin_collected_path = os.path.join('sound', 'coin_collected.wav')
        #self.bonus_collected_path = os.path.join('sound', 'plasterbrain.ogg')

        #Inicializa os objetos do tipo Som para ser manipulados pelo programa
        self.coin_collected = pygame.mixer.Sound(os.path.join('sound', 'coin_collected.wav'))
        self.bonus_collected = pygame.mixer.Sound(os.path.join('sound', 'plasterbrain.ogg'))
        self.music_menu = pygame.mixer.Sound(os.path.join('sound', 'retro_piano_menu_suspense.wav'))