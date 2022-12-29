class HiScoreList:
    """Pistelistastan ylläpidosta huolehtiva luokka
    """
    def __init__(self):
        """Luokan konstruktori, joka lisää alkuarvot pistelistalle tupleina."""
        self._hiscorelist = []
        self._hiscorelist.append(("Amalia", 19))
        self._hiscorelist.append(("Birgitta", 10))
        self._hiscorelist.append(("Cecilia", 5))
        self._hiscorelist.append(("Diana", 3))
        self._hiscorelist.append(("Elviira", 2))
        self.sort_list()

    def add_score(self, name, score):
        """Lisää uuden tuloksen pistelistalle ja järjestää listan sekä typistää sen pituuden viiteen riviin."

        Args:
            name (String): pelaajan nimi
            score (int): pelaajan pistemäärä
        """
        self._hiscorelist.append((name, score))
        self.sort_list()
        while len(self._hiscorelist) > 5:
            self._hiscorelist.pop()

    def sort_list(self):
        """Järjestää listan."""
        self._hiscorelist.sort(key=lambda item: item[1], reverse=True)

    def lines(self):
        """Palauttaa pistelista riveinä."""
        lines = []
        for score in self._hiscorelist:
            lines.append(f"{score[0]:15} {score[1]:>2}")
        return lines

    def __str__(self):
        """Tulostaan pistelistan. Käytetään testaukseen."""
        hiscorelist_string = ""
        for score in self._hiscorelist:
            hiscorelist_string += f"{score[0]:15} {score[1]:>2}\n"
        return hiscorelist_string