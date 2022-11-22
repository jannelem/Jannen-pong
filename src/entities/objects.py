import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, l):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, l)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, l):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, l)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)