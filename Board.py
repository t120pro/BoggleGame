from cube import Cube

class Board():
    dictionary = []
    
    def __init__(self):
        pass
        
    def createBoard(self):
        self._board = [[0 for x in range(5)] for y in range(5)]
        for x in range(5):
            for y in range(5):
                self._board[x][y] = Cube()
         
