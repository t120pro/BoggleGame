from Score import score


class ScoreBoard:

    def __init__(self):
        pass

    def update_board(self, user_score):
        score_board = open("score_board.txt", "r")
        lines = score_board.read().splitlines()

        for line in lines:
            name = line[0]
            scr = line[1]
            past_score = score(name, scr)

            if user_score.compare_to(past_score) >= 0:
                lines.add(score) #change it to put new score before past score
                last_line = lines[lines.len - 1]
                lines.remove(last_line)
            break

        score_board = open("score_board.txt", "w")
        score_board.write(user_score + "\n")
        score_board.close()

    def view_score_board(self):
        score_board = open("score_board.txt", "r")
        scores = score_board.read().splitlines()
        return scores
