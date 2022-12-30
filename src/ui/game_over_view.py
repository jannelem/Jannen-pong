import pygame


class GameOverView:
    """Pelin päättymisnäytöstä vastaava käyttöliittymäluokka.
    """

    def __init__(self, screen, bkg_color, object_color, screen_size, object_width, hi_scores, pong_service):
        """Luokan konstruktori.

        Args:
            screen (pygame.display): display-olio, jolle piirretään
            bkg_color (tuple): taustaväri
            object_color (tuple): tekstin väri
            screen_size (tuple): ruudun koko
            object_width (int): objektien koko
            hi_scores (HiScoreService): pistelistasta vastaava HiScoreService-olio
            pong_service (PongService): peliä hallinnoinut PongService-olio
        """
        self.bkg_color = bkg_color
        self.object_color = object_color
        self.screen = screen
        self.screen_size = screen_size
        self.object_width = object_width
        self.hi_scores = hi_scores
        self.pong_service = pong_service

    def run(self):
        """Pelin lopputuloksen näyttämisestä ja tarvittaessa pelaajan nimen tallentamisesta vastaava metodi.
        """

        pygame.init()

        font = pygame.font.SysFont("Arial", 36)
        player_name_input = "_"
        game_over_text = font.render(
            "Peli päättyi! (palaa painamalla Esc)", True, self.object_color)
        scores_text = font.render("Pisteet: pelaaja " + str(self.pong_service.scores()[
                                  0]) + ", tietokone " + str(self.pong_service.scores()[1]), True, self.object_color)
        new_hi_score_text = font.render(
            "Pääsit pistelistalle, anna nimesi + Enter:", True, self.object_color)
        player_name_text = font.render(
            player_name_input, True, self.object_color)

        clock = pygame.time.Clock()

        active = True

        while active:
            player_name_text = font.render(
                player_name_input, True, self.object_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    active = False
                if self.pong_service.check_new_hi_score():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            player_name_input = player_name_input[:-1]
                            self.hi_scores.add_new_score(
                                player_name_input, self.pong_service.scores()[0])
                            active = False
                        elif event.key == pygame.K_BACKSPACE and len(player_name_input) >= 2:
                            player_name_input = player_name_input[:-2]
                            player_name_input += "_"
                        elif event.key == pygame.K_COMMA:
                            pass
                        elif len(player_name_input) < 16:
                            player_name_input = player_name_input[:-1]
                            player_name_input += event.unicode
                            player_name_input += "_"

            self.screen.fill(self.bkg_color)
            self.screen.blit(game_over_text, (100, 50))
            self.screen.blit(scores_text, (100, 150))

            if self.pong_service.check_new_hi_score():
                self.screen.blit(new_hi_score_text, (100, 250))
                self.screen.blit(player_name_text, (100, 350))

            pygame.display.flip()
            clock.tick(60)
