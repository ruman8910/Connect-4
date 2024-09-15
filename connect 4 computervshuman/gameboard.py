class GameBoard:
    
    def __init__(self, num_rows=6, num_cols=7):
        self.__space = ' '
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__board =  []
            
        for i in range(self.__num_rows):
            row = [self.__space] * self.__num_cols
            self.__board.append(row)
    
    def get_lowest_empty_row_in_column(self, col):
        for row in range(self.__num_rows - 1, -1, -1):
            if self.is_space_free(row, col):
                return row
        return None
    
    def get_num_rows(self):
        return self.__num_rows
    
    def get_num_cols(self):
        return self.__num_cols
    
    def is_column_full(self, col): 
        return not self.is_space_free(0, col)

    def is_board_full(self):
        for row in self.__board:
            for space in row:
                if space == self.__space:
                    return False
        
    def is_space_free (self, row, col):
        
        return self.__board[row][col] == self.__space 
    
    def make_move(self, row, col, element):
        
        for r in range(self.__num_rows -1, -1, -1):
            if self.__board[r][col] == self.__space: 
                self.__board[r][col] = element 
                return 
        pass

    
    def save_game_state(self, file_path):
        with open(file_path, 'w') as file:
            for row in self.__board:
                file.write(' '.join(row) + '\n')
        print(f"Game state saved to {file_path}")

    def load_game_state(self, file_path):
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if i >= self.__num_rows:
                    break
                self.__board[i] = line.strip().split()
        print(f"Game state loaded from {file_path}")
    
    def show_board_dynamic(self):
            print("  1 | 2 | 3 | 4 | 5 | 6 | 7 |") 
            print("-------------------------------")
            for row in range(len(self.__board)): 
                print("|", end="")
                for col in range(len(self.__board[row])): 
                    print(" " + self.__board[row][col] + " |", end="")
                print("\n-------------------------------")
            
    pass
    



    def check_winner(self):
        return self.__check_winner_hz() or self.__check_winner_vt() or self.__check_winner_diag1() or self.__check_winner_diag2()
           
        
    
    def __check_winner_hz(self):

        for row in self.__board: 
            for col in range(self.__num_cols -3):
                if row [col] == row [col+1] == row [col+2] == row [col+3] != self.__space: 
                    return True
        return False 
    
    
    def __check_winner_vt(self):
        for col in range(self.__num_cols):
            for row in range(self.__num_rows - 3):
                if self.__board[row][col] == self.__board[row + 1][col] == self.__board[row + 2][col] == self.__board[row + 3][col] != self.__space: 
                    return True
        
        return False
    
    
    def __check_winner_diag1(self):
      
        
        for row in range(self.__num_rows - 3):  
            for col in range(self.__num_cols - 3):  
                if self.__board[row][col] == self.__board[row + 1][col + 1] == self.__board[row + 2][col + 2] == self.__board[row + 3][col + 3] != self.__space: 
                    return True
        return False 
    
    def __check_winner_diag2(self): 
       

        for row in range(self.__num_rows - 3): 
            for col in range(3, self.__num_cols):  
                if self.__board[row][col] == self.__board[row + 1][col - 1] == self.__board[row + 2][col - 2] == self.__board[row + 3][col - 3] != self.__space: 
                    return True
        return False



