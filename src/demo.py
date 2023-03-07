import fire
from grid import WordGrid
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"


def grid():
	print("┌────────────────────┐")
	print("│ Word Searcher 3000 │")
	print("└────────────────────┘")

def render_grid(dimension):
    grid_list = []
    for i in range(dimension):
        grid_list.append([])
        for j in range(dimension):
            grid_list[i].append(alphabet[random.randint(0,len(alphabet))])
    return grid_list
    
def print_grid(grid_list):
    grid()
    print_list = ""
    for row in grid_list:
        print_list = print_list + "\n"
        for letter in row:
            print_list = print_list + "  " + letter
    print(print_list)
    
word_list = ["able","about","above","accept"]
def add_words_into_grid(word_list):
    
    pass
if __name__ == '__main__':

  fire.Fire(print_grid(render_grid(15)))