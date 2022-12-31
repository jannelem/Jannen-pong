import pygame


class HiScoreView:
    """Pistelistan näyttämisestä vastaava käyttöliittymäluokka.
    """

    def __init__(self, screen, bkg_color, object_color, hi_scores):
        """Luokan konstruktori.

        Args:
            screen (pygame.display): display-olio, jolle piirretään
            bkg_color (tuple): taustaväri
            object_color (tuple): tekstin väri
            screen_size (tuple): ruudun koko
            hi_scores (HiScoreServive): HiScoreService-olio, joka tarjoaa parhaiden pisteiden listan.
        """
        self.bkg_color = bkg_color
        self.object_color = object_color
        self.screen = screen
        self.hi_scores = hi_scores

    def run(self):
        """Parhaiden pisteiden näyttämisestä ja näppäinten painalluksiin vastaamisesta huolehtiva metodi.
        """

        pygame.init()

        font = pygame.font.SysFont("Arial", 36)
        header_text = font.render(
            "Parhaat pisteet (palaa painamalla Esc):", True, self.object_color)
        start_game_text = font.render(
            "Aloita peli painamalla Enter", True, self.object_color)
        hiscores_texts = []
        for row in self.hi_scores.get_lines():
            hiscores_texts.append(font.render(row, True, self.object_color))

        clock = pygame.time.Clock()

        active = True

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    active = False

            self.screen.fill(self.bkg_color)
            row_y_coordinate = 50
            self.screen.blit(header_text, (100, row_y_coordinate))
            row_y_coordinate += 50
            for row in hiscores_texts:
                self.screen.blit(row, (100, row_y_coordinate))
                row_y_coordinate += 50

            pygame.display.flip()
            clock.tick(60)
