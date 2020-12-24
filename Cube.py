import random

class Cube():
    letters = ["E","E","E","E","E","E","E","E","E","E","A","A","A","A","A","A","A","A","I","I","I",
               "I","I","I","I","O","O","O","O","O","O","L","L","L","L","L","N","N","N","N","N","N",
               "S","S","S","S","S","S","T","T","T","T","T","T","T","D","D","D","D","R","R","R","R",
               "U","U","U","U","B","B","B","C","C","C","G","G","G","H","H","H","H","M","M","M","P",
               "P","P","Y","Y","Y","F","F","K","K","V","V","W","W","J","Qu","X","Z"]
    
    def __init__(self):
        self._value = random.choice(Cube.letters)
    
    def changeValue(self):
        self._value = random.choice(Cube.letters)
        
    def __str__(self):
        return self._value
