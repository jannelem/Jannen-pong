import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, l):
        super().__init__()
        self.rect = pygame.Rect(x,y,w,l)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
    
    def move_up(self, step, height):
        self.y = self.y - step
        if self.y < step:
            self.y = step
    
    def move_down(self, step, height):
        self.y += step
        if self.y > height - self.h - step:
            self.y = height - self.h - step

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)