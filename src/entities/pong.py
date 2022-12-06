import pygame
from entities.objects import Paddle
from entities.objects import Ball


class Pong:

    def __init__(self, bkg_color, object_color, screen_size, object_width):
        self.running = True

        self.player_paddle = Paddle(
            bkg_color, object_color, object_width, object_width*10)
        self.player_paddle.rect.x = 20
        self.player_paddle.rect.y = screen_size[1] / \
            2 - self.player_paddle.rect.height/2

        self.computer_paddle = Paddle(
            bkg_color, object_color, object_width, object_width*10)
        self.computer_paddle.rect.x = screen_size[0]-20-object_width
        self.computer_paddle.rect.y = screen_size[1] / \
            2 - self.computer_paddle.rect.height/2

        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.player_paddle)
        self.paddles.add(self.computer_paddle)

        self.ball = Ball(bkg_color, object_color, object_width)
        self.ball.rect.x = screen_size[0]/2-self.ball.rect.width/2
        self.ball.rect.y = screen_size[1]/2-self.ball.rect.height/2

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.paddles)
        self.all_sprites.add(self.ball)
