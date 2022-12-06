import pygame
from ui.game_view import GameView


class MenuView:

    def __init__(self, screen, bkg_color, object_color, screen_size, object_width):
        self.bkg_color = bkg_color
        self.object_color = object_color
        self.screen = screen
        self.screen_size = screen_size
        self.object_width = object_width

    def run(self):

        pygame.init()

        font = pygame.font.SysFont("Arial", 36)
        first_row_text = font.render(
            "Tervetuloa pelaamaan Pongia!", True, self.object_color)
        start_game_text = font.render(
            "Aloita peli painamalla Enter", True, self.object_color)
        close_window_text = font.render(
            "Lopeta peli painamalla Esc", True, self.object_color)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.start_pong()
            if keys[pygame.K_ESCAPE]:
                break

            self.screen.fill(self.bkg_color)
            self.screen.blit(first_row_text, (100, 50))
            self.screen.blit(start_game_text, (100, 150))
            self.screen.blit(close_window_text, (100, 250))
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    def start_pong(self):
        game_view = GameView(self.screen, self.bkg_color,
                             self.object_color, self.screen_size, self.object_width)
        game_view.run()
