from cube import Cube

class Board():
    
    def __init__(self):
        self.create_board()
        
    def create_board(self):
        self._board = [[0 for x in range(5)] for y in range(4)]
        for y in range(5):
            for x in range(4):
                self._board[x][y] = Cube()
