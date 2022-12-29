from entities.hi_score_list import HiScoreList


class HiScoreService:
    """Pistelistan tietoja muokkaava luokka."""
    def __init__(self):
        """Konstruktori, joka luo listan.
        """
        self._scores = HiScoreList()

    def lowest_score(self):
        """Palauttaa listan pienimmän pistemäärän, jota suuremmalla tuloksella pääsee listalle."""
        return self._scores._hiscorelist[(len(self._scores._hiscorelist)-1)][1]

    def add_new_score(self, name, score):
        """Lisää tuloksen pistelistaan."""
        self._scores.add_score(name, score)

    def get_lines(self):
        """Palauttaa pistelistan tiedot merkkijonolistana."""
        return self._scores.lines()
