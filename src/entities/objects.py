from random import randint
import pygame


class Paddle(pygame.sprite.Sprite):
    """Pelin mailan toiminnallisuudesta vastaava luokka, joka pohjautuu pygame-kirjaston luokkaan Sprite.

    """

    def __init__(self, bkg_color, paddle_color, width, height):
        """Luokan konstruktori, joka luo uuden mailan.

        Args:
            bkg_color (tuple): taustan väri
            paddle_color (tuple): mailan väri
            width (int): mailan leveys pikseleinä
            height (int): mailan korkeus pikseleinä
        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(bkg_color)
        self.image.set_colorkey(bkg_color)

        pygame.draw.rect(self.image, paddle_color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move_up(self, step_size):
        """Siirtää mailaa ylöspäin määritetyn step_sizen verran, mutta varmistaa ettei mailan y-koordinaatti mene nollaa pienemmäksi.

        Args:
            step_size (int): määrä, jolla mailan y-koordinaattia muutetaan.
        """
        self.rect.y -= step_size
        self.rect.y = max(self.rect.y, 0)

    def move_down(self, step_size, screen_size):
        """Siirtää mailaa alaspäin määritetyn step_sizen verran, mutta varmistaa ettei maila päädy näytön alareunan ulkopuolelle.

        Args:
            step_size (int): määrä, jolla mailan y-koordinaattia muutetaan
            screen_size (_type_): ruudun koko
        """
        self.rect.y += step_size
        self.rect.y = min(self.rect.y, screen_size[1]-self.rect.height)


class Ball(pygame.sprite.Sprite):
    """Pelin pallon toiminnallisuudesta vastaava luokka, joka pohjautuu pygame-kirjaston luokkaan Sprite.
    """

    def __init__(self, bkg_color, object_color, object_width):
        """Luokan konstruktori, joka luo uuden pallon, joka sijaitsee keskellä ruutua ja saa satunnaisen nopeuden.

        Args:
            bkg_color (tuple): taustaväri
            object_color (tuple): pallon väri
            object_width (int): pallon koko
        """
        super().__init__()
        self.image = pygame.Surface([object_width, object_width])
        self.image.fill(bkg_color)
        self.image.set_colorkey(bkg_color)
        pygame.draw.rect(self.image, object_color, [
                         0, 0, object_width, object_width])
        self.velocity = [randint(-8, 8), randint(-8, 8)]
        while self.velocity[0] == 0:
            self.velocity[0] = randint(-8, 8)
        self.rect = self.image.get_rect()

    def update(self):
        """Muuttaa pallon x- ja y- koordinaatteja nopeuden osoittamalla määrällä eli siirtää palloa.
        """
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        """Muuttaa pallon nopeutta satunnaisesti sen törmätessä mailaan siten, että pallon nopeuden vaakasuora komponentti vaihtaa suuntaansa.
        """
        if self.velocity[0] > 0:
            self.velocity[0] = randint(-8, -1)
        elif self.velocity[0] < 0:
            self.velocity[0] = randint(1, 8)
        self.velocity[1] = randint(-8, 8)
