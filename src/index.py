import pygame
from entities.objects import Paddle
from entities.objects import Ball

pygame.init()

# colors:
BKG_COLOR = (0, 0, 0)
OBJECT_COLOR = (0, 255, 255)
OBJECT_WIDTH = 10


screen_size = (640, 480)
game_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption = ("Jannen Pong")

RUNNING = True

clock = pygame.time.Clock()

player_paddle = Paddle(BKG_COLOR, OBJECT_COLOR, OBJECT_WIDTH, OBJECT_WIDTH*10)
player_paddle.rect.x = 20
player_paddle.rect.y = screen_size[1]/2 - player_paddle.rect.height/2

computer_paddle = Paddle(BKG_COLOR, OBJECT_COLOR,
                         OBJECT_WIDTH, OBJECT_WIDTH*10)
computer_paddle.rect.x = screen_size[0]-30
computer_paddle.rect.y = screen_size[1]/2 - computer_paddle.rect.height/2

paddles = pygame.sprite.Group()
paddles.add(player_paddle)
paddles.add(computer_paddle)

ball = Ball(BKG_COLOR, OBJECT_COLOR, OBJECT_WIDTH, OBJECT_WIDTH)
ball.rect.x = screen_size[0]/2-ball.rect.width/2
ball.rect.y = screen_size[1]/2-ball.rect.height/2


all_sprites = pygame.sprite.Group()
all_sprites.add(paddles)
all_sprites.add(ball)

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move_up(OBJECT_WIDTH)
    if keys[pygame.K_DOWN]:
        player_paddle.move_down(OBJECT_WIDTH, screen_size)

# sovelluslogiikkaa

    all_sprites.update()

    if ball.rect.x >= screen_size[0]-ball.rect.width or ball.rect.x <= 0:
        ball.velocity[0] *= -1
    if ball.rect.y >= screen_size[1] - ball.rect.height or ball.rect.y <= 0:
        ball.velocity[1] *= -1

    if computer_paddle.rect.center[1] > ball.rect.center[1]:
        computer_paddle.move_up(OBJECT_WIDTH)
    elif computer_paddle.rect.center[1] < ball.rect.center[1]:
        computer_paddle.move_down(OBJECT_WIDTH, screen_size)

    for paddle in paddles:
        if pygame.sprite.collide_mask(ball, paddle):
            ball.bounce()

# piirtäminen

    game_screen.fill(BKG_COLOR)
    pygame.draw.line(game_screen, OBJECT_COLOR, [
                     screen_size[0]/2, 0], [screen_size[0]/2, screen_size[1]-1], 5)
    all_sprites.draw(game_screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
