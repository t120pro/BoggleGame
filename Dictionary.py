_dictionary = []

def import_dictionary():
    dict_file = open("webster_word_list.txt", "r")
    global _dictionary
    _dictionary = dict_file.read().splitlines()
    dict_file.close()

def does_word_exist(word):
    if word in _dictionary:
        return True
    else:
        return False

#should this method be here?
def add_to_word(self, letter):
    self._current_word.append(letter)
