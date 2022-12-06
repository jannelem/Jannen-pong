import pygame
from ui.menu_view import MenuView


def main():
    bkg_color = (0, 0, 0)
    object_color = (0, 255, 255)
    object_width = 10
    screen_size = (640, 480)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption = ("Jannen Pong")

    view = MenuView(screen, bkg_color, object_color, screen_size, object_width)
    view.run()


if __name__ == "__main__":
    main()
