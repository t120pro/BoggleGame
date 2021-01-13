from cube import Cube

class Board():
    
    def __init__(self):
        self.create_board()
        
    def create_board(self):
        self._board = [[0 for x in range(4)] for y in range(5)]
        for y in range(4):
            for x in range(5):
                self._board[x][y] = Cube()
            
    def print_board(self):
        print("______________\n")
        for y in range(4):
            for x in range(5):
                print(self._board[x][y], end=" ")
                if self._board[x][y] != "Qu":
                    print(" ", end="")
            if y != 3:
                print("\n")
        print("\n______________")
            
    def get_board(self):
        return self._board
    
    def get_by_index(self, x, y):
        return self._board[x][y]
