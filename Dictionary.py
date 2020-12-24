class Dictionary():
    dictionary = []
    
    def __init__(self):
        pass

    def saveDictionary(self):
        dict_file = open("webster_word_list.txt", "r")
        Board.dictionary = dict_file.read().splitlines()
        dict_file.close()
    
    def doesWordExist(self, word):
        if word in Board.dictionary:
            return True
        else:
            return False
    
    def addToWord(self, letter):
        self._current_word.append(letter)
    

