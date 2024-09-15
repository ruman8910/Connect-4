from tkinter import messagebox, Button, Tk
from gameboard import GameBoard
from player import HumanPlayer, ComputerPlayer
import time     

class GameGUI:

    def __init__(self, player1_type, player2_type, color, grid_size):
        self.mw = Tk()
        self.mw.configure(bg="light blue")  
        self.gboard = GameBoard(num_rows=grid_size, num_cols=grid_size)
        self.buttons_2d_list = []  
        self.players_lst = []  
        self.current_player_index = 0
        self.winner = False
        self.player1_type = player1_type
        self.player2_type = player2_type
        self.color = color

        # Call methods to initialize the game
        self.create_buttons()
        self.create_players()
        self.handle_computer_turn()

        self.mw.mainloop()

    def create_buttons(self):
        for i in range(self.gboard.get_num_rows()):
            row = []
            for j in range(self.gboard.get_num_cols()):
                button = Button(self.mw, text=" ", command=lambda row=i, col=j: self.clicked_btn(col), height=5, width=10, bg="light blue")
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons_2d_list.append(row)

        # Create restart button
        self.restart_button = Button(self.mw, text="Restart", command=self.restart_game, bg="lightcoral", fg="white", relief="raised")
        self.restart_button.grid(row=self.gboard.get_num_rows() + 2, column=0, columnspan=self.gboard.get_num_cols(), pady=10, padx=5)

    def create_players(self):
        if self.color == "yellow":
            p1_symbol = "O"
            p2_symbol = "X"
        else:
            p1_symbol = "X"
            p2_symbol = "O"

        if self.player1_type == "human":
            p1 = HumanPlayer(p1_symbol, self.gboard, game_gui=self)
        else:
            p1 = ComputerPlayer(p1_symbol, self.gboard, self.buttons_2d_list, game_gui=self)
        if self.player2_type == "human":
            p2 = HumanPlayer(p2_symbol, self.gboard, game_gui=self)
        else:
            p2 = ComputerPlayer(p2_symbol, self.gboard, self.buttons_2d_list, game_gui=self)

        self.players_lst = [p1, p2]

    def handle_computer_turn(self):
        current_player = self.players_lst[self.current_player_index]
        if isinstance(current_player, ComputerPlayer):
            current_player.play()
            self.switch_player() 

        if not self.winner and not self.gboard.is_board_full(): 
            self.mw.after(2000, self.handle_computer_turn())
    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players_lst)
    def clicked_btn(self, col):
        player = self.players_lst[self.current_player_index]
        button = self.buttons_2d_list[0][col]
        row = self.gboard.get_lowest_empty_row_in_column(col)

        if row is not None:
            if button["state"] != "disabled" or row > 1:  
                if self.gboard.is_space_free(row, col):
                    self.gboard.make_move(row, col, player.get_player_symbol())  
                    self.update_button_text(row, col, player.get_player_symbol()) 
                    self.gboard.save_game_state("game_state.txt") 
                    winner = self.gboard.check_winner()
                    if winner:
                        win_message = f"Player {player.get_player_symbol()} is the Winner!"
                        messagebox.showinfo("Winner Info", win_message)
                        self.mw.destroy()
                    elif self.gboard.is_board_full():
                        messagebox.showinfo("Winner Info", "The Game Has Ended In A Draw!")
                        self.mw.destroy()
                    else:
                        self.switch_player()  
                        self.handle_computer_turn()  
            elif isinstance(player, ComputerPlayer):
                self.mw.after(2000, self.handle_computer_turn) 
        else:
            print("Column is full, cannot drop disc.")

    def update_button_text(self, row, col, element):
        if row is not None:
            button_color = "yellow" if element == "O" else "red" if self.color == "red" else "yellow"

            for i in range(self.gboard.get_num_rows()):
                button = self.buttons_2d_list[i][col]
                if i <= row: 
                    button.config(bg=button_color) 
                else:  
                    current_color = button.cget("bg")  
                    r, g, b = self.mw.winfo_rgb(current_color) 
                    r = max(0, r - 1000)  
                    g = max(0, g - 1000)
                    b = max(0, b - 1000)
                    new_color = "#{:02x}{:02x}{:02x}".format(r // 256, g // 256, b // 256)  
                    button.config(bg=new_color)  
                self.mw.update() 
                time.sleep(0.05) 

            self.buttons_2d_list[row][col].config(state="disabled")
            self.buttons_2d_list[self.gboard.get_lowest_empty_row_in_column(col)][col].config(bg=button_color)
            for i in range(row):
                button = self.buttons_2d_list[i][col]
                button.config(bg="light blue")  
        else:
            print("Column is full, cannot drop disc.")

    def restart_game(self):
        self.mw.destroy() 
        game_gui = GameGUI(self.player1_type, self.player2_type, self.color, self.gboard.get_num_cols())
