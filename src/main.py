import random
from grid import Grid 
from word import Word
from colorama import Fore
from sqlalchemy import create_engine
from sqlalchemy.orm import Session , session_maker

from sqlalchemy import Table
from sqlalchemy import inspect


alphabet = "abcdefghijklmnopqrstuvwxyz"

found_color_regex = "\033[1;33m"
def heading():
	print("┌────────────────────┐")
	print("│ Word Searcher 3000 │")
	print("└────────────────────┘")


def print_grid(grid_list):
    heading()
    #starting the text with all back colors
    print_list = f"{Fore.BLACK}"
    test_list = ""
    for row in grid_list:
        print_list = print_list + "\n"
        for letter in row:
            print_list = print_list + "  " + letter
            test_list = test_list+letter
    print_list = print_list +" "
    print(print_list)
    return test_list

    

def check_guess(guess,word_list, grid , start_color_regex = Fore.GREEN, end_color_regex = Fore.BLACK):
    for each_word in word_list:
        if guess.lower() == each_word.text.lower():
            each_word.found = True
            for i,j in each_word.coordinates:
                grid.matrix[i][j] = f"{start_color_regex}{grid.matrix[i][j]}{end_color_regex}"


    print_grid(grid.matrix)
    
    #we want to return word list because we modify if each word found is true
    return word_list
    
def run_evertyhing(difficulty):

    return difficulty

if __name__ == '__main__':
    

    engine = create_engine("sqlite:///word_list.db")
    
    with Session(engine) as session:
        session.query()

    ###################################
    # The below two lines are inplace of SQL input
    #####################################
    word_list = ["able","about","above","accept", "momhole"]

    word_list = [Word(_) for _ in word_list]
    
    #initializing that all words are not found (default is false)
    for word in word_list:
        word.found = False

    #geting the grid to actually initialize
    testGrid = Grid(15)
    testGrid.add_words(word_list)

        
    #present table    
    print_grid(testGrid.matrix)
    
    while not all([_.found for _ in word_list]):
        guess = input('Enter a word! : ')
        word_list = check_guess(guess, word_list, testGrid)

