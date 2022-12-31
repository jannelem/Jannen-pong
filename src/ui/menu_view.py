import pygame
from ui.game_view import GameView
from ui.hi_score_view import HiScoreView
from services.hi_score_service import HiScoreService


class MenuView:
    """Pelin päävalikosta vastaava käyttöliittymäluokka.
    """

    def __init__(self, screen, bkg_color, object_color, screen_size, object_width):
        """Luokan konstruktori.

        Args:
            screen (pygame.display): display-olio, jolle piirretään
            bkg_color (tuple): taustaväri
            object_color (tuple): tekstin väri
            screen_size (tuple): ruudun koko
            object_width (int): objektien koko
            hi_scores (HiScoreService): pistelistasta huolehtiva HiScoreService-olio
        """
        self.bkg_color = bkg_color
        self.object_color = object_color
        self.screen = screen
        self.screen_size = screen_size
        self.object_width = object_width
        self.hi_scores = HiScoreService()

    def run(self):
        """Valikon näyttämisestä ja näppäinten painalluksiin vastaamisesta huolehtiva metodi.
        """

        pygame.init()

        font = pygame.font.SysFont("Arial", 36)
        first_row_text = font.render(
            "Tervetuloa pelaamaan Pongia!", True, self.object_color)
        start_game_text = font.render(
            "Aloita peli painamalla Enter", True, self.object_color)
        hiscores_text = font.render(
            "Katso parhaat pisteet painamalla H", True, self.object_color)
        close_window_text = font.render(
            "Lopeta peli painamalla Esc", True, self.object_color)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.start_pong()
                    if event.key == pygame.K_h:
                        self.show_high_scores()
                    elif event.key == pygame.K_ESCAPE:
                        exit()

            self.screen.fill(self.bkg_color)
            self.screen.blit(first_row_text, (100, 50))
            self.screen.blit(start_game_text, (100, 150))
            self.screen.blit(hiscores_text, (100, 250))
            self.screen.blit(close_window_text, (100, 350))
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    def start_pong(self):
        """Käynnistää pelin.
        """
        game_view = GameView(self.screen, self.bkg_color,
                             self.object_color, self.screen_size, self.object_width, self.hi_scores)
        game_view.run()

    def show_high_scores(self):
        """Näyttää parhaiden pisteiden listan."""
        hi_score_view = HiScoreView(self.screen, self.bkg_color,
                                    self.object_color, self.hi_scores)
        hi_score_view.run()
