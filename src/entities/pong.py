import pygame
from entities.objects import Paddle
from entities.objects import Ball


class Pong:

    """Pelin tietosisällöstä vastaava luokka.

        Attributes:
            player_paddle (Paddle): pelaajan maila
            computer_paddle (Paddle): tietokoneen maila
            ball (Ball): pelin pallo
            paddles: mailat sisältävä ryhmä
            all_sprites: mailat ja pallon sisältävä ryhmä
            running (boolean): True, jos peli on meneillään ja False, jos peli on päättynyt

    """

    def __init__(self, bkg_color, object_color, screen_size, object_width):
        """Luokan konstruktori, joka luo pelin mailat ja pallon.

        Args:
            bkg_color (tuple): taustaväri
            object_color (tuple): pallon ja mailojen väri
            screen_size (tuple): ruudun koko
            object_width (int): mailojen ja pallon koko
        """
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
