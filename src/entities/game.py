import pygame

WIDTH = 20

class Game():
    def __init__(self, window_size):
        self.running = True

        self.ball = objects.Ball(window_size[0]/2-WIDTH/2, window_size[1]/2-WIDTH/2, WIDTH)
        self.player = objects.Paddle(window_size[0]/2-2*WIDTH, 0, WIDTH, 4*WIDTH)
        self.computer = objects.Paddle(0, window_size[1]/2-2*WIDTH, WIDTH, 4*WIDTH)
        self.upper_wall = objects.Wall(0, 0, window_size[0], WIDTH)
        self.lower_wall = objects.Wall(0, window_size[1]-WIDTH, window_size[0], WIDTH)

        self.walls = pygame.sprite.Group()
        self.walls.add(self.upper_wall)
        self.walls.add(self.lower_wall)

        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.player)
        self.paddles.add(self.computer)

        self.all_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.walls, self.paddles, self.ball)
