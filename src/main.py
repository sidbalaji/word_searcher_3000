import random
from grid import Grid 
from word import Word
from colorama import Fore
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
 
from sqlalchemy import Table
from sqlalchemy import inspect
from sql_words import Easy_Words, Medium_Words, Difficult_Words

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
    
def run_evertyhing(difficulty, grid_size = 15, num_words = 5):
    word_list = []
    engine = create_engine("sqlite:///word_list.db")

    if difficulty.lower() == 'easy':
        tbl = Easy_Words
    elif difficulty.lower() == 'medium':
        tbl = Medium_Words

    with Session(engine) as session:
        for n in range(num_words):
            rand = random.randrange(0, session.query(tbl).count())
            row = session.query(tbl)[rand]
            word_list.append(row)
    
    if difficulty.lower() == 'easy':  
        word_list = [Word(_.easy_words) for _ in word_list]
    elif difficulty.lower() == 'medium':
        word_list = [Word(_.medium_words) for _ in word_list]

    
    #initializing that all words are not found (default is false)
    for word in word_list:
        word.found = False

    #geting the grid to actually initialize
    testGrid = Grid(grid_size)
    testGrid.add_words(word_list)

    print_grid(testGrid.matrix)
    print([_.text for _ in word_list])        
    while not all([_.found for _ in word_list]):
        guess = input('Enter a word! : ')
        word_list = check_guess(guess, word_list, testGrid)
        print([_.text for _ in word_list])        


    
    return 0

if __name__ == '__main__':
    run_evertyhing('medium', grid_size=20, num_words=10)

    
        
        

    ###################################
    # The below two lines are inplace of SQL input
    #####################################

    

        
    #present table    
