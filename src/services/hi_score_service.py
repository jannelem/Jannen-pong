from entities.hi_score_list import HiScoreList


class HiScoreService:
    def __init__(self):
        self._scores = HiScoreList()

    def lowest_score(self):
        return self._scores._hiscorelist[(len(self._scores._hiscorelist)-1)][1]

    def add_new_score(self, name, score):
        self._scores.add_score(name, score)

    def get_lines(self):
        return self._scores.lines()
