from tkinter import Tk
from connect4_setup_gui import Connect4SetupGUI
from gamegui import GameGUI
from gameboard import GameBoard
from player import HumanPlayer, ComputerPlayer

def main():
    gboard = GameBoard()
    p1 = HumanPlayer("X", gboard)
    p2 = ComputerPlayer("O", gboard) 
    players_lst = (p1, p2)  
    winner = False
    
    gboard.show_board_dynamic()
    
    while not winner:
        for p in players_lst:
            p.play()
            gboard.show_board_dynamic()
            
            winner = gboard.check_winner()
            if winner:
                print(f"Congratulations Player {p.get_player_symbol()} wins!")
                break

            if gboard.is_board_full():
                print("The Board Is Full, Game Has Ended In Draw!")
                break

if __name__ == "__main__":
    print("Welcome to Connect4!")
    while True:
        print("Choose interface:")
        print("\t 1. Console")
        print("\t 2. GUI")
        choice = input("Enter number to choose interface or q to quit: ")
        if choice.lower() == "q":
            break
        elif choice == "1":
            print("")
            main()
        elif choice == "2":
            root = Tk()  
            app = Connect4SetupGUI(root)  
            root.mainloop()  

            if app.grid_size_spinbox.get() == "6x7":
                main()  # Run the console version
            else:
                game_gui = GameGUI(app.player1_type_var.get(), app.player2_type_var.get(), app.color_var.get(), int(app.grid_size_spinbox.get()))
                game_gui.run()  # Run the GUI version
