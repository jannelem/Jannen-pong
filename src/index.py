import pygame
import entities.game
import entities.objects


BKG_COLOR = (0,0,0)
OBJECT_COLOR = (0,0,255)
window_size = (640, 480)

def main():
    pygame.init()
    display = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Jannen Pong")
    game = entities.game.Game(window_size)
    game.all_sprites.draw(display)

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()