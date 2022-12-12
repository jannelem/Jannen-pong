import pygame
from entities.pong import Pong


class PongService:
    """Luokka, joka muokkaa pelin Pong-luokan tietosisältöä ja jonka metodeita kutsutaan käyttöliittymäluokista.
    """
    def __init__(self, bkg_color, object_color, screen_size, object_width):
        """Konstruktori, joka alustaa olion ja luo pelin.

        Args:
            bkg_color (tuple): taustaväri
            object_color (tuple): mailojen ja pallon väri
            screen_size (tuple): ruudun koko
            object_width (int): mailojen ja pallon koko
        """
        self.pong = Pong(bkg_color, object_color, screen_size, object_width)
        self.screen_size = screen_size
        self.object_width = object_width

    def player_move_up(self):
        """Metodi, jota kutsutaan käyttöliittymästä pelaajan liikuttaessa mailaansa ylöspäin.
        """
        self.pong.player_paddle.move_up(self.object_width)

    def player_move_down(self):
        """Metodi, jota kutsutaan käyttöliittymästä pelaajan liikuttaessa mailaansa alaspäin.
        """
        self.pong.player_paddle.move_down(self.object_width, self.screen_size)

    def _computer_move(self):
        """Tietokoneen mailan liikuttamisesta vastaava metodi, joka liikuttaa mailaa pystysuunnassa siten, että mailan keskikohta olisi kohdakkain pallon kanssa. Maila liikkuu silloin, kun pallo on tietokoneen puolella ruutua ja pallo on liikkumassa tietokoneen mailan suuntaan.
        """
        if self.pong.ball.velocity[0] > 0 and self.pong.ball.rect.x >= self.screen_size[0]/2:
            if self.pong.computer_paddle.rect.center[1] > self.pong.ball.rect.center[1]:
                self.pong.computer_paddle.move_up(self.object_width//2)
            elif self.pong.computer_paddle.rect.center[1] < self.pong.ball.rect.center[1]:
                self.pong.computer_paddle.move_down(
                    self.object_width//2, self.screen_size)

    def _handle_wall_collisions(self):
        """Muuttaa pallon nopeutta sen törmätessä seiniin."""
        if self.pong.ball.rect.x >= self.screen_size[0]-self.pong.ball.rect.width or \
                self.pong.ball.rect.x <= 0:
            self.pong.ball.velocity[0] *= -1
        if self.pong.ball.rect.y >= self.screen_size[1] - self.pong.ball.rect.height or \
                self.pong.ball.rect.y <= 0:
            self.pong.ball.velocity[1] *= -1

    def _handle_paddle_collisions(self):
        """Tarkistaa, törmääkö pallo pelaajan tai tietokoneen mailaan. Pallon törmätessä kutsuu pallon bounce-metodia."""
        for paddle in self.pong.paddles:
            if pygame.sprite.collide_mask(self.pong.ball, paddle):
                self.pong.ball.bounce()

    def handle_game_events(self):
        """Suorittaa pelin kierroksen aikana tietokoneen mailan siirron ja käsittelee törmäyksen seinien ja mailojen kanssa."""
        self._computer_move()
        self._handle_wall_collisions()
        self._handle_paddle_collisions()

    def running(self):
        """_summary_

        Returns:
            True, jos peli on käynnissä. False, jos peli on päättynyt.
        """
        return self.pong.running

    def stop(self):
        """Pysäyttää pelin
        """
        self.pong.running = False

    def sprites(self):
        """Palauttaa listan pelin objekteista.

        Returns:
            Lista, joka sisältää pelin mailat ja pallon.
        """
        return self.pong.all_sprites
