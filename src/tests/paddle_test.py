import unittest
from entities.objects import Paddle


class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle((0, 0, 0), (0, 255, 255), 15, 100)
        self.paddle.rect.y = 100

    def test_paddle_moves_up(self):
        self.paddle.move_up(10)
        self.assertEqual(self.paddle.rect.y, 90)

    def test_paddle_does_not_move_up_beyond_screen(self):
        self.paddle.move_up(101)
        self.assertEqual(self.paddle.rect.y, 0)

    def test_paddle_moves_down(self):
        self.paddle.move_down(100, (640, 480))
        self.assertEqual(self.paddle.rect.y, 200)

    def test_paddle_does_not_move_down_beyond_screen(self):
        self.paddle.move_down(400, (640, 480))
        self.assertEqual(self.paddle.rect.y, 380)
