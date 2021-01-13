from cube import Cube
from board import Board
from score import Score
import time
from score_board import Score_Board
import dictionary

def main_menu():
    print("\n-----Main Menu:-----")
    response = str(input("Do you wish to (1) View the Scores, (2) Play!, or (3) Quit?  "))
    if response == "1":
        view_scores()
    elif response == "2":
        play_boggle()
    else:
        print("Thanks for playing.")
        sys.exit()
        
def play_boggle():
    print("\n-----Play Game:-----")
    name = str(input("Enter you name: "))
    board = Board()
    score = Score(name, 0)
    score_board = Score_Board()
    start_time = time.time()
    print("The game will begin. You have 60 seconds to enter any words you see. Only real words will be added to your score. Words must be 3 or more letters. Good Luck!!")
    while time.time() - start_time < 60:
        board.print_board()
        word = input("Enter a word: ")
        if (time.time() - start_time > 60):
            break;
        if (dictionary.does_word_exist(word.lower())):
            indexes = []
            for i in range(len(word)):
                
                letter = word[i]
                for y in range(4):
                    for x in range(5):
                        if (str(board.get_by_index(x, y)) == letter.capitalize() and [x, y] not in indexes):
                            if len(indexes) == i:
                                indexes.append([x, y])
                                
            if len(indexes) == len(word): # if full word is found on board
                score.add_points(word)
                for i in indexes:
                    board.get_by_index(i[0], i[1]).changeValue()
            else:
                print("Your word isn't on the board")
                
    print("Your score is: " + str(score.get_score()))
    
    # checking if made high score
    score_board.update_board(score)
    view_scores()

def view_scores():
    score_board = Score_Board()
    print("\n-----Score Board:-----")
    score_board.print_scores()
    main_menu()
    
def main():
    dictionary.import_dictionary()
    main_menu() 
    cube1 = Cube()
    cube1.changeValue()
        
main()
