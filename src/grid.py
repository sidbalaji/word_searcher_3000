import random

# string representation of alphabet, used to randomly populate the crossword matrix
alphabet = "abcdefghijklmnopqrstuvwxyz"

def move_right(i,j):
    # Utility function to move from "cell to cell" and add in word to grind
    return i+1 , j

def move_left(i,j):
    # Utility function to move from "cell to cell" and add in word to grind
    return i-1 , j

def move_up(i,j):
    # Utility function to move from "cell to cell" and add in word to grind
    return i , j-1

def move_down(i,j):
    # Utility function to move from "cell to cell" and add in word to grind
    return i , j+1



class Grid:
    """_summary_
    """
    def __init__(self, dimension):
        """
        Dimension (INT) -> size of the grid (one side)
        """
        self.dimension = dimension
        self.matrix = self.render_matrix(self.dimension)
        self.coordinates_with_words = []
    
    def render_matrix(self, dimension):
        """Creates a list of lists whcih is the 
        grid of letters that will make up the body of crossword

        Args:
            dimension (int): what the dimension of the crossword shoudl be
            we are assuming a square grid

        Returns:
            _type_: list of lists
        """

        grid_list = []
        # for loop creates n-rows
        for i in range(dimension):
            grid_list.append([])
            #for loop adds n-characters to each empty list
            for j in range(dimension):
                grid_list[i].append(alphabet[random.randint(0,25)])
        #returning a square
        return grid_list


    
    def add_words(self, word_list):
        """
        Function to populate the crossword 
        adds all words into crossword by replacing 
        cells (holding random characters) with the
        letters we want add in 
        
        Args:
            word_list (list of Word types): _description_

        Returns:
            _type_: list of lists
        """
        self.word_list = word_list
        self.word_check_list = [_.text for _ in word_list]
        
        for word in word_list:
            #pick either veritcal or horizontal as direction the word is rendered in
            direction = random.choice(['vertical', 'horizontal', 'diagonal'])
            
            word.direction = direction
            
            #call the function that actually adds letters into the crossword
            self.add_word(word)
        
        return self.matrix
    
    
    
    def add_word(self, word):
        """Function that takes in a Word type and add the characters to the crossword

        Args:
            word (Word type): object containing the text of a word, list of characters in the word, etc.
        """
        word.coordinates = []
        
        #overlap means that the randomly chosen point in the grid has already been filled in by the characters of a different word that we wanted to add in to the crossword
        overlap = True
        
        while overlap:
            # check if the randomly generated location conflicts the location of an already instered character
            (i,j), overlap = self.get_new_starting_coordinates_and_check(word)
            
        
        #############################################
        ### Below block of code is to "insert" the characters in the desired order/shape
        #############################################
        
        #HORIZONTAL CASE
        if word.direction == 'horizontal':
            for character in word.characters:
                self.matrix[i][j] = character
                word.coordinates.append((i,j))
                self.coordinates_with_words.append((i,j))
                
                i,j = move_down(i,j)

        #DIAGONAL CASE
        if word.direction == 'diagonal':
            for character in word.characters:
                self.matrix[i][j] = character
                word.coordinates.append((i,j))
                self.coordinates_with_words.append((i,j))
                
                intermediate_i , intermediate_j = move_down(i,j)
                i,j = move_right(intermediate_i , intermediate_j)
                
        #VERTICAL CASE
        elif word.direction == 'vertical':
            for character in word.characters:
                self.matrix[i][j] = character
                word.coordinates.append((i,j))
                self.coordinates_with_words.append((i,j))
                i,j = move_right(i,j)


    
    def get_starting_coords(self, word):
        """helper function to get create start coordinates 
        for randomly inserting word into crossword matrix
        
        Also checks that you dont start a word in a space where there is not enough room to fit full word
        
        Args:
            word (Word): a word type 

        Returns:
            i , j (int): coordinates for where word will start
        """
        i = random.choice(range(0,len(self.matrix) - len(word.characters)))
        j = random.choice(range(0,len(self.matrix) - len(word.characters)))
        return i , j

    def project_coordinates(self, starting_point, word):
        """A helper function that will checks if the starting coordintes for 
        a word will result in a previously written word to overwritten

        Args:
            starting_point (tuple of 2 ints): (i,j) location of starting point
            word (Word): uses the "direction" of a word to calculte projected coordinates of each letter

        Returns:
            bool: returns a true or false depending of if there is a conflict or not
        """
        i,j = starting_point
        list_of_coordinates = []
        list_of_coordinates.append((i,j))
        
        if word.direction == 'horizontal':
            for character in word.characters:
                i,j = move_down(i,j)
                list_of_coordinates.append((i,j))
        
        if word.direction == 'diagonal':
            for character in word.characters:
                intermediate_i , intermediate_j = move_down(i,j)
                i,j = move_right(intermediate_i , intermediate_j)

                list_of_coordinates.append((i,j))


        elif word.direction == 'vertical':
            for character in word.characters:
                i,j = move_right(i,j)
                list_of_coordinates.append((i,j))
        
        return any(x in list_of_coordinates for x in self.coordinates_with_words)

    def get_new_starting_coordinates_and_check(self, word):
        """wrapper function used to re simulate a new starting coordinate
         if there is a overlap for previous coordinate

        Args:
            word (_type_): _description_

        Returns:
            _type_: _description_
        """
        i, j  = self.get_starting_coords(word)
        overlap = self.project_coordinates((i,j), word)
        
        return (i,j) , overlap
        
        

