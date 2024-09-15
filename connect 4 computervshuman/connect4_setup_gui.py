
from tkinter import Tk, Label, Button, StringVar, OptionMenu, Spinbox
from gamegui import GameGUI

class Connect4SetupGUI:
    def __init__(self, master):
        self.master = master
        master.title("Connect 4 Setup")

        self.label = Label(master, text="Welcome to Connect 4 Setup!")
        self.label.pack()

        self.player1_type_var = StringVar(master)
        self.player1_type_var.set("human") 
        self.player1_label = Label(master, text="Player 1 type:")
        self.player1_label.pack()
        self.player1_type_menu = OptionMenu(master, self.player1_type_var, "human", "computer")
        self.player1_type_menu.pack()

        self.player2_type_var = StringVar(master)
        self.player2_type_var.set("human") 
        self.player2_label = Label(master, text="Player 2 type:")
        self.player2_label.pack()
        self.player2_type_menu = OptionMenu(master, self.player2_type_var, "human", "computer")
        self.player2_type_menu.pack()

        self.color_var = StringVar(master)
        self.color_var.set("red") 
        self.color_label = Label(master, text="Choose your color:")
        self.color_label.pack()
        self.color_menu = OptionMenu(master, self.color_var, "red", "yellow")
        self.color_menu.pack()
 
        self.grid_size_label = Label(master, text="Select grid size:")
        self.grid_size_label.pack()
        self.grid_size_spinbox = Spinbox(master, from_=4, to=10, increment=1)
        self.grid_size_spinbox.pack()

        self.play_button = Button(master, text="Play", command=self.start_game)
        self.play_button.pack()

    def start_game(self):
        player1_type = self.player1_type_var.get()
        player2_type = self.player2_type_var.get()
        color = self.color_var.get()
        grid_size = int(self.grid_size_spinbox.get())
        game_gui = GameGUI(player1_type, player2_type, color, grid_size)



def main():
    root = Tk()
    app = Connect4SetupGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()