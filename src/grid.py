import random


alphabet = "abcdefghijklmnopqrstuvwxyz"

def move_right(i,j):
    return i+1 , j

def move_left(i,j):
    return i-1 , j

def move_up(i,j):
    return i , j-1

def move_down(i,j):
    return i , j+1



class Grid:
    def __init__(self, dimension):
        
        self.dimension = dimension
        self.matrix = self.render_matrix(self.dimension)
        self.coordinates_with_words = []
    
    def render_matrix(self, dimension):
        grid_list = []
        for i in range(dimension):
            grid_list.append([])
            for j in range(dimension):
                grid_list[i].append(alphabet[random.randint(0,25)])
        return grid_list


    
    def add_words(self, word_list):
        self.word_list = word_list
        self.word_check_list = [_.text for _ in word_list]
        
        for word in word_list:
            #pick either veritcal or horizontal as direction the word is rendered in
            direction = random.choice(['vertical', 'horizontal', 'diagonal'])
            
            word.direction = direction
            
            self.add_word(word)
        
        return self.matrix
    
    
    
    def add_word(self, word):
        #find dimensions for where you can start the word
        #so we will need:
        #        - length of word
        #        - length of row/column (we are assumign square word searches)
        word.coordinates = []
        
        
        overlap = True
        
        while overlap:
            (i,j), overlap = self.get_new_starting_coordinates_and_check(word)
            
        #check if the 
        
        
        if word.direction == 'horizontal':
            for character in word.characters:
                self.matrix[i][j] = character
                word.coordinates.append((i,j))
                self.coordinates_with_words.append((i,j))
                
                i,j = move_down(i,j)

        if word.direction == 'diagonal':
            for character in word.characters:
                self.matrix[i][j] = character
                word.coordinates.append((i,j))
                self.coordinates_with_words.append((i,j))
                
                intermediate_i , intermediate_j = move_down(i,j)
                i,j = move_right(intermediate_i , intermediate_j)
                
                
        elif word.direction == 'vertical':
            for character in word.characters:
                self.matrix[i][j] = character
                word.coordinates.append((i,j))
                self.coordinates_with_words.append((i,j))
                i,j = move_right(i,j)


    
    def get_starting_coords(self, word):
        i = random.choice(range(0,len(self.matrix) - len(word.characters)))
        j = random.choice(range(0,len(self.matrix) - len(word.characters)))
        return i , j

    def project_coordinates(self, starting_point, word):
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
        i, j  = self.get_starting_coords(word)
        overlap = self.project_coordinates((i,j), word)
        
        return (i,j) , overlap
        
        

