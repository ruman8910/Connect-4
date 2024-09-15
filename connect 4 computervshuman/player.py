import random
import time

class Player:
    
    def __init__(self, symbol, board):
        self.__symbol = symbol
        self._gboard = board
        
    def get_player_symbol(self):
        return self.__symbol
    

class HumanPlayer(Player):
    
    def __init__(self, symbol, board, game_gui=None):
        super().__init__(symbol, board)
        self.__symbol = symbol
        self.game_gui = game_gui

    def play(self):
        if self.game_gui:
            self.play_gui_move()
        else:
            self.play_console_move()

    def play_gui_move(self):
        print("Player %s turn" % self.get_player_symbol())
        while True:
            try:
                col = int(input("Please enter column number (1-7): ")) - 1  
                if col < 0 or col >= self._gboard.get_num_cols():
                    print("Invalid column number. Please enter a number between 1 and %d." % self._gboard.get_num_cols())
                    continue  # Continue the loop to prompt the user again
                    
                if not self._gboard.is_column_full(col):
                    row = self._gboard.get_lowest_empty_row_in_column(col)
                    if row is not None:
                        element = self.get_player_symbol()  # Get the player's symbol
                        self._gboard.make_move(row, col, element)  # Pass the element as an argument
                        break
                    else:
                        print("Column is full. Please choose another column.")
                else:
                    print("Column is full. Please choose another column.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_console_move(self):
        print("Player %s turn" % self.get_player_symbol())
        while True:
            try:
                col = int(input("Please enter column number (1-7): ")) - 1  
                if col < 0 or col >= self._gboard.get_num_cols():
                    print("Invalid column number. Please enter a number between 1 and %d." % self._gboard.get_num_cols())
                    continue  # Continue the loop to prompt the user again
                    
                if not self._gboard.is_column_full(col):
                    row = self._gboard.get_lowest_empty_row_in_column(col)
                    if row is not None:
                        element = self.get_player_symbol()  # Get the player's symbol
                        self.make_move(row, col, element)  # Use the console-specific make_move method
                        break
                    else:
                        print("Column is full. Please choose another column.")
                else:
                    print("Column is full. Please choose another column.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def make_move(self, row, col, element):
        self._gboard.make_move(row, col, element)


class ComputerPlayer(Player):
    
    def __init__(self, symbol, board, buttons_2d_list=None, game_gui=None):
        super().__init__(symbol, board)
        self.buttons_2d_list = buttons_2d_list
        self.game_gui = game_gui

    def play(self):
        if self.buttons_2d_list: 
            self.game_gui.mw.after(2000, self.__play_with_gui_delay)  
        else:
            self.__play_without_gui_delay()

    def __play_with_gui_delay(self):
        print("Player %s turn" % self.get_player_symbol())
        while True:
            col = random.randint(0, self._gboard.get_num_cols() - 1)
            if not self._gboard.is_column_full(col):
                row = self._gboard.get_lowest_empty_row_in_column(col)
                if row is not None:
                    element = self.get_player_symbol()
                    self._gboard.make_move(row, col, element)  
                    self.game_gui.update_button_text(row, col, element)  
                    break

    def __play_without_gui_delay(self):
        print("Player %s turn" % self.get_player_symbol())
        while True:
            col = random.randint(0, self._gboard.get_num_cols() - 1)
            if not self._gboard.is_column_full(col):
                row = self._gboard.get_lowest_empty_row_in_column(col)
                if row is not None:
                    element = self.get_player_symbol()
                    self._gboard.make_move(row, col, element)
                    break

