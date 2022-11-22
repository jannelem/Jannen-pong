import pygame
import entities.game
import entities.objects


BKG_COLOR = (0,0,0)
OBJECT_COLOR = (0,255,255)
window_size = (640, 480)

def main():
    pygame.init()
    display = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Jannen Pong")
    game = entities.game.Game(window_size)
    clock = pygame.time.Clock()

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.player.move_up(20, window_size[1])
            elif event.type == pygame.QUIT:
                game.running = False
        
        display.fill(BKG_COLOR)

        for sprite in game.all_sprites:
            pygame.draw.rect(display, OBJECT_COLOR, sprite.rect)
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()