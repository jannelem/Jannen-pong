import unittest
from entities.hi_score_list import HiScoreList


class TestHiScoreList(unittest.TestCase):
    def setUp(self):
        self.test_list = HiScoreList()

    def test_new_list_length_is_correct(self):
        self.assertEqual(len(self.test_list.lines()), 5)

    def test_new_hi_score_is_saved(self):
        self.test_list.add_score("Irmeli", 10)
        new_name_found = False
        for line in self.test_list.lines():
            if line.find("Irmeli") != -1:
                new_name_found = True
        self.assertEqual(new_name_found, True)

    def test_new_hi_score_is_not_saved_if_score_too_low(self):
        self.test_list.add_score("Irmeli", 1)
        new_name_found = False
        for line in self.test_list.lines():
            if line.find("Irmeli") != -1:
                new_name_found = True
        self.assertEqual(new_name_found, False)

    def test_list_is_length_is_correct_after_adding_new_score(self):
        self.test_list.add_score("Irmeli", 10)
        self.assertEqual(len(self.test_list.lines()), 5)

    def test_scores_are_in_correct_order_after_adding_new_score(self):
        tuples = self.test_list.tuples()
        for i in range(1, len(tuples)):
            self.assertLessEqual(tuples[i][1], tuples[i-1][1])
