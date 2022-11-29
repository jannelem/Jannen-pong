import unittest
from entities.objects import Ball


class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball((0, 0, 0), (0, 255, 255), 10, 10)

    def test_ball_exists(self):
        self.assertNotEqual(self.ball, None)

    def test_ball_moves(self):
        (x, y) = (self.ball.rect.x, self.ball.rect.y)
        self.ball.update()
        self.assertNotEqual((x, y), (self.ball.rect.x, self.ball.rect.y))

    def test_ball_bounces_back(self):
        old_velocity_x = self.ball.velocity[0]
        self.ball.bounce()
        self.assertEqual(self.ball.velocity[0], -old_velocity_x)
