import unittest
from entities.objects import Ball


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball((0, 0, 0), (0, 255, 255), 10)

    def test_ball_exists(self):
        self.assertNotEqual(self.ball, None)

    def test_ball_moves(self):
        (x, y) = (self.ball.rect.x, self.ball.rect.y)
        self.ball.update()
        self.assertNotEqual((x, y), (self.ball.rect.x, self.ball.rect.y))

    def test_ball_bounces_left(self):
        self.ball.velocity[0] = 1
        self.ball.bounce()
        self.assertLess(self.ball.velocity[0], 0)
    
    def test_ball_bounces_right(self):
        self.ball.velocity[0] = -1
        self.ball.bounce()
        self.assertGreater(self.ball.velocity[0], 0)