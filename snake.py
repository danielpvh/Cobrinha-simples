"""
Criado por Daniel Cunha em 5 de Julho de 2019
"""

import  pygame, random, apple, inimigo, state, sound
import constants as c

inimigo.criar_inimigo(11)
a = apple.Apple()


class Snake():



    def __init__(self, pscreen):

        self.screen = pscreen

        self.clock = pygame.time.Clock()
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.snake_skin = pygame.Surface((10, 10))
        self.snake_skin.fill((c.WHITE))

        self.score = 0

        self.fonte = c.FONT_DEFAULT
        self.score_render = self.fonte.render(str(self.score), True, c.WHITE)

        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3
        self.my_direction = self.LEFT

    def on_grid_random(self):
        x = random.randint(0, 670)
        y = random.randint(0, 450)
        return (x // 10 * 10, y // 10 * 10)

    def collision(self, c1, c2):
        return (c1[0] == c2[0] and (c1[1] == c2[1]))

    def render(self):
        self.screen.fill(c.BLACK)

        #Chama a funcao do objeto apple e apple_blue para renderizar na tela junto com a snake
        a.render(self.screen)

        #Chama a funcao para atualizar os pontos na tela do jogo
        self.update(self.score)



        self.clock.tick(20)
        if self.my_direction == self.UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - 10)
        if self.my_direction == self.DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + 10)
        if self.my_direction == self.LEFT:
            self.snake[0] = (self.snake[0][0] - 10, self.snake[0][1])
        if self.my_direction == self.RIGHT:
            self.snake[0] = (self.snake[0][0] + 10, self.snake[0][1])

        for pos in self.snake:
            self.screen.blit(self.snake_skin, pos)

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i - 1][0], self.snake[i - 1][1])

        #COLISAO COLISAO COLISAO COLISAO APPLE, APPLE
        if self.collision(self.snake[0], a.apple_pos):
            sound.Sound().coin_collected.play()
            a.apple_pos = self.on_grid_random()
            self.snake.append((0, 0))
            self.score += 10
        #VERIFICA SE A SNAKE COLIDIU COM ALGUM INIMIGO DA LISTA ALEATORIA SOMENTE QUANDO MOSTRADO NA TELA, a.teste
        for i in range(0, len(inimigo.lista_inimigos)):
            if (self.collision(self.snake[0],(inimigo.lista_inimigos[i].pos_y, inimigo.lista_inimigos[i].pos_x))) and a.colission:
                state.State().setstate('QUIT GAME')

        #COLISAO COLISAO APPLE_BLUE
        if self.collision(self.snake[0], a.apple_blue_pos):
            sound.Sound().bonus_collected.play()
            a.apple_blue_last_pos = list(a.apple_blue_pos)
            #Atribui o valor 500 para sair do loop e nao renderizar mais na tela
            a.apple_blue_time_render = 500
            #Adiciona o objeto na lista snake para faze-la crescer a cada colisao
            self.snake.append((0, 0))
            #Gera uma posicao aleatoria para o apple_blue_pos
            a.apple_blue_pos = self.on_grid_random()
            self.score += 500
            a.mostra_bonus_switch = True


    #Atualiza os ponto na tela
    def update(self, score):

        self.score_render = self.fonte.render(str(score), True ,c.WHITE)
        self.screen.blit(self.score_render, (600, -5))


