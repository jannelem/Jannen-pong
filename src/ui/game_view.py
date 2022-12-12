import pygame
from services.pong_service import PongService


class GameView:
    """Pelaamisen aikaiseta näkymästä vastaava käyttöliittymäluokka.

    Attributes:
        pong_service (PongService): pelin tietojen muokkaamisesta vastaava olio
    """

    def __init__(self, screen, bkg_color, object_color, screen_size, object_width):
        """Luokan konstruktori, joka alustaa pelin.

        Args:
            screen (pygame.display): pygamen ruutu
            bkg_color (tuple): taustaväri
            object_color (tuple): pallon ja mailojen väri
            screen_size (tuple): ruudun koko
            object_width (int): pallon ja mailojen koko
        """
        self.pong_service = PongService(
            bkg_color, object_color, screen_size, object_width)
        self.bkg_color = bkg_color
        self.object_color = object_color
        self.screen = screen
        self.screen_size = screen_size
        self.object_width = object_width

    def run(self):
        """Pelin etenemisestä vastaava metodi, joka sisältää pelisilmukan.
        """

        pygame.init()
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Arial", self.object_width*2)
        while self.pong_service.running():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pong_service.stop()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.pong_service.player_move_up()
            if keys[pygame.K_DOWN]:
                self.pong_service.player_move_down()
            
            scores = self.pong_service.scores()
            scores_string = "Pelaaja: " + str(scores[0]) + " Tietokone: " + str(scores[1]) + ", paina Esc lopettaaksesi"
            scores_text = font.render(scores_string, True, self.object_color)

            self.pong_service.handle_game_events()
            self.pong_service.sprites().update()

            self.screen.fill(self.bkg_color)
            pygame.draw.line(self.screen, self.object_color, [self.screen_size[0]//2, 0], [
                             self.screen_size[0]//2, self.screen_size[1]-1], self.object_width//2)
            self.screen.blit(scores_text, (self.screen_size[0]//10, self.screen_size[1]-2*self.object_width))
            self.pong_service.sprites().draw(self.screen)
        
            pygame.display.flip()

            clock.tick(60)
