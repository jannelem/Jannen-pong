import unittest
from entities.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game((640, 480))

    def test_newly_created_game_is_running(self):
        self.assertEqual(self.game.running, True)
