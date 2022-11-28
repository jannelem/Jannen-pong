from random import randint
import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, bkg_color, paddle_color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(bkg_color)
        self.image.set_colorkey(bkg_color)

        pygame.draw.rect(self.image, paddle_color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move_up(self, step_size):
        self.rect.y -= step_size
        self.rect.y = max(self.rect.y, 0)

    def move_down(self, step_size, screen_size):
        self.rect.y += step_size
        self.rect.y = min(self.rect.y, screen_size[1]-self.rect.height)


class Ball(pygame.sprite.Sprite):

    def __init__(self, bkg_color, object_color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(bkg_color)
        self.image.set_colorkey(bkg_color)
        pygame.draw.rect(self.image, object_color, [0, 0, width, height])
        self.velocity = [randint(-8, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] *= -1
        self.velocity[1] = randint(-8, 8)
