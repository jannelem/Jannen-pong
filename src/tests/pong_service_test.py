import unittest
from services.pong_service import PongService
from services.hi_score_service import HiScoreService


class TestPongService(unittest.TestCase):
    def setUp(self):
        self.pong_service = PongService(
            (0, 0, 0), (0, 255, 255), (640, 480), 10, HiScoreService())

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

    def test_computer_moves_down(self):
        self.pong_service.pong.computer_paddle.rect.y = 100
        self.pong_service.pong.ball.rect.x = 400
        self.pong_service.pong.ball.rect.y = 200
        self.pong_service.pong.ball.velocity = [1, 1]
        self.pong_service._computer_move()
        self.assertEqual(self.pong_service.pong.computer_paddle.rect.y, 105)

    def test_computer_moves_up(self):
        self.pong_service.pong.computer_paddle.rect.y = 200
        self.pong_service.pong.ball.rect.x = 400
        self.pong_service.pong.ball.rect.y = 100
        self.pong_service.pong.ball.velocity = [1, 1]
        self.pong_service._computer_move()
        self.assertEqual(self.pong_service.pong.computer_paddle.rect.y, 195)

    def test_ball_bounces_from_horizontal_wall(self):
        self.pong_service.pong.ball.rect.x = 100
        self.pong_service.pong.ball.rect.y = 5
        self.pong_service.pong.ball.velocity = [5, -5]
        self.pong_service.pong.ball.update()
        self.pong_service._handle_wall_collisions()
        self.assertEqual(self.pong_service.pong.ball.velocity[1], 5)

    def test_ball_bounces_from_vertical_wall(self):
        self.pong_service.pong.ball.rect.x = 635
        self.pong_service.pong.ball.rect.y = 5
        self.pong_service.pong.ball.velocity = [5, -5]
        self.pong_service.pong.ball.update()
        self.pong_service._handle_wall_collisions()
        self.assertEqual(self.pong_service.pong.ball.velocity[0], -5)

    def test_ball_does_not_bounce_without_collision(self):
        old_velocity = self.pong_service.pong.ball.velocity
        self.pong_service.handle_game_events()
        self.assertEqual(self.pong_service.pong.ball.velocity, old_velocity)

    def test_ball_bounces_from_player_paddle(self):
        self.pong_service.pong.ball.velocity = [-4, 0]
        self.pong_service.pong.ball.rect.x = 60
        self.pong_service.pong.ball.rect.y = 120
        self.pong_service.pong.player_paddle.rect.x = 50
        self.pong_service.pong.player_paddle.rect.y = 100
        self.pong_service.sprites().update()
        self.pong_service._handle_paddle_collisions()
        self.assertGreater(self.pong_service.pong.ball.velocity[0], 0)

    def test_check_new_hi_score_returns_true(self):
        self.pong_service.pong.scores = [3, 17]
        self.assertEqual(self.pong_service.check_new_hi_score(), True)

    def test_check_new_hi_score_returns_false(self):
        self.pong_service.pong.scores = [2, 18]
        self.assertEqual(self.pong_service.check_new_hi_score(), False)

    def test_game_ends_when_scored(self):
        self.pong_service.pong.scores = [10, 9]
        self.pong_service._player_scores()
        self.pong_service.handle_game_events()
        self.assertEqual(self.pong_service.running(), False)

    def test_game_continues_when_scored(self):
        self.pong_service.pong.scores = [10, 8]
        self.pong_service._computer_scores()
        self.assertEqual(self.pong_service.running(), True)
