import random
from grid import Grid 
from word import Word
from colorama import Fore
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from sql_words import Easy_Words, Medium_Words, Difficult_Words, Pokemon
import argparse

alphabet = "abcdefghijklmnopqrstuvwxyz"

found_color_regex = "\033[1;33m"
normal_header = """
             .--.            .---.           .-.
         .---|--|    .-.     | W |  .------. |~|    .--.
      .--|===|Se|----|_|--.__| O |--|::::::| |~|-==-|==|---.
      |~~| W |ar|====| |~~|--| R |--| WILL |_|~|    |  |___|-.
      |  | O |ch|====| |==|  | D |  |::::::|=| |    |  |---|=|
      |  | R |er|3000|_|__|  | S |__|BE HAD| | |    |  |___| |
      |~~| D |--|====|~|~~|==|~~~|--|::::::|=|~|----|==|---|=|
      ^--^---'--^----^-^--^--^---'--^------^-^-^-==-^--^---^-'
    
"""
pokemon_header = """
                                  ,'\\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
"""

def heading(pokemon_heading):
    # print(text)
    if pokemon_heading: 
        print(pokemon_header)
    else:
        print(normal_header)
    # print("┌────────────────────────┐")
	# print("│ Pokemon Searcher 3000 │")
	# print("└────────────────────────┘")

def print_grid(grid_list,pokemon_heading):
    heading(pokemon_heading)
    #starting the text with all back colors
    print_list = f"{Fore.WHITE}"
    test_list = ""
    for row in grid_list:
        print_list = print_list + "\n"
        for letter in row:
            print_list = print_list + "  " + letter
            test_list = test_list+letter
    print_list = print_list +" "
    print(print_list)
    return test_list

    

def check_guess(guess,word_list, grid,pokemon_heading , start_color_regex = Fore.GREEN, end_color_regex = Fore.WHITE):
    for each_word in word_list:
        if guess.lower() == each_word.text.lower():
            each_word.found = True
            for i,j in each_word.coordinates:
                grid.matrix[i][j] = f"{start_color_regex}{grid.matrix[i][j]}{end_color_regex}"


    print_grid(grid.matrix, pokemon_heading)
    
    #we want to return word list because we modify if each word found is true
    return word_list
    
def run_evertyhing(difficulty, grid_size = 15, num_words = 5):
    word_list = []
    engine = create_engine("sqlite:///word_list.db")

    if difficulty.lower() == 'easy':
        tbl = Easy_Words
    elif difficulty.lower() == 'medium':
        tbl = Medium_Words
    elif difficulty.lower() == 'difficult':
        tbl = Difficult_Words
    elif difficulty.lower() == 'pokemon':
        tbl = Pokemon
    else:
        tbl = Pokemon

    with Session(engine) as session:
        for n in range(num_words):
            rand = random.randrange(0, session.query(tbl).count())
            row = session.query(tbl)[rand]
            word_list.append(row)
    
    if difficulty.lower() == 'easy':  
        word_list = [Word(_.easy_words) for _ in word_list]
    elif difficulty.lower() == 'medium':
        word_list = [Word(_.medium_words) for _ in word_list]
    elif difficulty.lower() == 'difficult':
        word_list = [Word(_.difficult_words) for _ in word_list]
    elif difficulty.lower() == 'pokemon':
        word_list = [Word(_.pokemon_names) for _ in word_list]
    else:
        word_list = [Word(_.pokemon_names) for _ in word_list]
    #initializing that all words are not found (default is false)
    for word in word_list:
        word.found = False

    #geting the grid to actually initialize
    testGrid = Grid(grid_size)
    testGrid.add_words(word_list)

    pokemon_heading = False if difficulty.lower() in ['easy', 'medium', 'difficult'] else True
    print_grid(testGrid.matrix , pokemon_heading = pokemon_heading)
    print([_.text for _ in word_list])        
    while not all([_.found for _ in word_list]):
        guess = input('Enter a word! : ')
        os.system("clear")

        word_list = check_guess(guess, word_list, testGrid, pokemon_heading)
        print([_.text for _ in word_list])



    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    

    parser.add_argument("difficulty", type=str, default='pokemon')
    parser.add_argument("--grid_size", type=int, default=25)
    parser.add_argument("--num_words", type=int, default=8)

    args = parser.parse_args()
    print(args)

    run_evertyhing(args.difficulty, args.grid_size, args.num_words)

    
        
