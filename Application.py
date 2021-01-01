from score import Score
from score_board import Score_Board

from tkinter import *
import tkinter.font as tkFont

class Application(Frame):
    def __init__(self, master, img):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets(img)
        
    def create_widgets(self, img):
        #setting up logo
        canvas = Canvas(self, width = 750, height = 200, bg='white')                
        canvas.create_image(380 ,100, image=img)
        canvas.grid(row=0, column=0, columnspan=2)

        #self.create_main_menu()
        #self.boggle_board()
        self.score_board()

    def create_main_menu(self):
        
        # create play button
        mm_play = Button(self,
               text = "LET'S PLAY!",
               bg = "white",
               bd = 4,
               activebackground = "black",
               activeforeground = "white",
               font = app_font
               #command = self.tell_story
               )
        mm_play.grid(row=1, column=0, columnspan=2)
        
        # create high score button
        mm_high_score = Button(self,
               text = "SCORES",
               bg = "white",
               bd = 4,
               activebackground = "black",
               activeforeground = "white",
               font = app_font
               #command = self.tell_story
               )
        mm_high_score.grid(row=2, column=0, columnspan=2)
        
        # create high score button
        mm_quit = Button(self,
               text = "QUIT",
               bg = "white",
               bd = 4,
               activebackground = "black",
               activeforeground = "white",
               font = app_font,
               command = self.quit_game
               )
        mm_quit.grid(row=3, column=0, columnspan=2)
    
    def score_board(self):
         pass       
    
    def boggle_board(self):
        pass
    
    def quit_game(self):
        sys.exit()

# main
root = Tk()
root.title("Boogle")
root.geometry("750x600")
root['background']='white'
img = PhotoImage(file="boggle_logo.gif")

app_font = tkFont.Font(family="Helvetica",size=20,weight="bold")
app = Application(root, img)
root.mainloop()
