from score import Score

class Score_Board:

    def __init__(self):
        #saving score_board.txt by creating a list of scores
        score_board = open("score_board.txt", "r")
        lines = score_board.read().splitlines()
        self._high_scores = []

        for i in range(len(lines)):
            line = str(lines[i]).split("~")
            name = line[0]
            score = line[1]
            self._high_scores.append(Score(name, score))
    
    def get_high_scores(self):
        return self._high_scores
    
    def update_board(self, user_score):
        #inserting user's score into score board
        for i in range(10):
            if len(self._high_scores) <= i or user_score.compare_to(self._high_scores[i]) >= 0:
                self._high_scores.insert(i, user_score)
                break
        
        #saving new board to file
        score_board = open("score_board.txt", "w")
        for high_score in self._high_scores:
            score_board.write(str(high_score) + "\n")
        score_board.close()
