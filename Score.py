class Score:

    def __init__(self, name, score):
        self._name = name
        self._score = int(score)

    def __str__(self):
        return self._name + "~" + str(self._score)

    def compare_to(self, other):
        if self._score < other._score:
            return -1
        elif self._score == other._score:
            return 0
        else:
            return 1
        
    def get_score(self):
        return self._score
    def get_name(self):
        return self._name
    
    def add_points(word):
        if len(word) > 2:
            self._score += len(word)
