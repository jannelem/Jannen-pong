import unittest
from services.pong_service import PongService

class TestPongService(unittest.TestCase):
    def setUp(self):
        self.pong_service = PongService((0,0,0), (0,255,255), (640,480), 10)

    def test_player_moves_up(self):
        self.pong_service.player_move_up()
        self.assertEqual(self.pong_service.pong.player_paddle.rect.y, 180)
    
    def test_player_does_not_move_up_beyond_screen(self):
        for i in range(1000):
            self.pong_service.player_move_up()
        self.assertEqual(self.pong_service.pong.player_paddle.rect.y, 0)
    
    def test_player_moves_down(self):
        self.pong_service.player_move_down()
        self.assertEqual(self.pong_service.pong.player_paddle.rect.y, 200)
    
    def test_player_does_not_move_down_beyond_screen(self):
        for i in range(1000):
            self.pong_service.player_move_down()
        self.assertEqual(self.pong_service.pong.player_paddle.rect.y, 380)
    
    def test_game_is_running(self):
        self.assertEqual(self.pong_service.running(), True)
    
    def test_game_stops_running(self):
        self.pong_service.stop()
        self.assertEqual(self.pong_service.running(), False)
    
    def test_correct_number_of_sprites(self):
        self.assertEqual(len(self.pong_service.sprites()), 3)