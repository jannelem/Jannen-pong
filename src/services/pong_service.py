import pygame
from entities.pong import Pong


class PongService:
    def __init__(self, bkg_color, object_color, screen_size, object_width):
        self.pong = Pong(bkg_color, object_color, screen_size, object_width)
        self.screen_size = screen_size
        self.object_width = object_width

    def player_move_up(self):
        self.pong.player_paddle.move_up(self.object_width)

    def player_move_down(self):
        self.pong.player_paddle.move_down(self.object_width, self.screen_size)

    def _computer_move(self):
        if self.pong.ball.velocity[0] > 0 and self.pong.ball.rect.x >= self.screen_size[0]/2:
            if self.pong.computer_paddle.rect.center[1] > self.pong.ball.rect.center[1]:
                self.pong.computer_paddle.move_up(self.object_width//2)
            elif self.pong.computer_paddle.rect.center[1] < self.pong.ball.rect.center[1]:
                self.pong.computer_paddle.move_down(
                    self.object_width//2, self.screen_size)

    def _handle_wall_collisions(self):
        if self.pong.ball.rect.x >= self.screen_size[0]-self.pong.ball.rect.width or \
                self.pong.ball.rect.x <= 0:
            self.pong.ball.velocity[0] *= -1
        if self.pong.ball.rect.y >= self.screen_size[1] - self.pong.ball.rect.height or \
                self.pong.ball.rect.y <= 0:
            self.pong.ball.velocity[1] *= -1

    def _handle_paddle_collisions(self):
        for paddle in self.pong.paddles:
            if pygame.sprite.collide_mask(self.pong.ball, paddle):
                self.pong.ball.bounce()

    def handle_game_events(self):
        self._computer_move()
        self._handle_wall_collisions()
        self._handle_paddle_collisions()

    def running(self):
        return self.pong.running

    def stop(self):
        self.pong.running = False

    def sprites(self):
        return self.pong.all_sprites
