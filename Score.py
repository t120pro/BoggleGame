class score:

    __name = ""
    __high_score = 0

    def __init__(self, name, high_score):
        __name = name
        __high_score = high_score

    def __str__(self):
        return self.__name + " " + self.high_score

    def compare_to(self, other):
        if self.__high_score < other.high_score:
            return -1
        elif self.__high_score == other.high_score:
            return 0
        else:
            return 1
