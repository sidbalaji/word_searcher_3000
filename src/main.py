import random
from grid import Grid 
from word import Word
from colorama import Fore

alphabet = "abcdefghijklmnopqrstuvwxyz"

found_color_regex = "\033[1;33m"
def heading():
	print("┌────────────────────┐")
	print("│ Word Searcher 3000 │")
	print("└────────────────────┘")


def print_grid(grid_list):
    heading()
    print_list = ""
    test_list = ""
    for row in grid_list:
        print_list = print_list + "\n"
        for letter in row:
            print_list = print_list + "  " + letter
            test_list = test_list+letter
    print_list = print_list +" "
    print(print_list)
    return test_list

    

if __name__ == '__main__':
    start_color_regex = Fore.RED
    end_color_regex = Fore.BLACK



    ###################################
    # The below two lines are inplace of SQL input
    #####################################
    word_list = ["able","about","above","accept", "momhole"]
    text_word_list = ["able","about","above","accept"]
    word_list = [Word(_) for _ in word_list]
    #geting the grid to actually initialize
    testGrid = Grid(15)

    testGrid.add_words(word_list)
    
    #present table
        
    #present table
    
    print_grid(testGrid.matrix)
    guess = input('Enter a word! : ')
    if guess in text_word_list:
        print('cool')
        
        for each_word in testGrid.word_list:
        
            for i,j in each_word.coordinates:
                testGrid.matrix[i][j] = f"{start_color_regex}{testGrid.matrix[i][j]}{end_color_regex}"
        
        print_grid(testGrid.matrix)