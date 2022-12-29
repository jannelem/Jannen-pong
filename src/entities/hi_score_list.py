class HiScoreList:
    def __init__(self):
        self._hiscorelist = []
        self._hiscorelist.append(("Amalia", 10))
        self._hiscorelist.append(("Birgitta", 5))
        self._hiscorelist.append(("Cecilia", 3))
        self._hiscorelist.append(("Diana", 2))
        self._hiscorelist.append(("Elviira", 1))
        self._hiscorelist.sort(key=lambda item: item[1], reverse=True)

    def add_score(self, name, score):
        self._hiscorelist.append((name, score))
        self._hiscorelist.sort(key=lambda item: item[1], reverse=True)
        while len(self._hiscorelist) > 5:
            self._hiscorelist.pop()

    def lines(self):
        lines = []
        for score in self._hiscorelist:
            lines.append(f"{score[0]:15} {score[1]:>2}")
        return lines

    def __str__(self):
        hiscorelist_string = ""
        for score in self._hiscorelist:
            hiscorelist_string += f"{score[0]:15} {score[1]:>2}\n"
        return hiscorelist_string


if __name__ == "__main__":
    hslist = HiScoreList()
    print(hslist)
    hslist.add_score("Janne", 73)
    hslist.add_score("Pirjo", 49)
    print(hslist)
    print("Rivien tulostus:")
    for line in hslist.lines():
        print(line)
