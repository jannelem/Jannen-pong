import unittest
from services.hi_score_service import HiScoreService


class TestHiScoreService(unittest.TestCase):
    def setUp(self):
        self.hi_score_service = HiScoreService()

    def test_lowest_score_is_correct_in_new_list(self):
        self.assertEqual(self.hi_score_service.lowest_score(), 2)

    def test_lowest_score_does_not_change(self):
        self.hi_score_service.add_new_score("Irmeli", 1)
        self.assertEqual(self.hi_score_service.lowest_score(), 2)

    def test_lowest_score_changes(self):
        old_lowest_score = self.hi_score_service.lowest_score()
        self.hi_score_service.add_new_score("Pirjo", 7)
        self.assertGreater(
            self.hi_score_service.lowest_score(), old_lowest_score)

    def test_correct_number_of_lines_returned(self):
        self.assertEqual(len(self.hi_score_service.get_lines()), 5)

    def test_number_of_lines_does_not_change_when_getting_lowest_score(self):
        self.hi_score_service.lowest_score()
        self.assertEqual(len(self.hi_score_service.get_lines()), 5)

    def test_number_of_lines_does_not_change_when_adding_new_score(self):
        self.hi_score_service.add_new_score("Vilja", 10)
        self.assertEqual(len(self.hi_score_service.get_lines()), 5)
