import unittest
from entities.pong import Pong


class TestPong(unittest.TestCase):
    def setUp(self):
        self.pong = Pong((0, 0, 0), (0, 255, 255), (640, 580), 10)

    def test_new_game_is_running(self):
        self.assertEqual(self.pong.running, True)

    def test_both_paddles_exist(self):
        self.assertEqual(len(self.pong.paddles), 2)

    def test_ball_exists(self):
        self.assertNotEqual(self.pong.ball, None)
