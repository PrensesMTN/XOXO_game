import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.create_buttons()


    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font='normal 20 bold', height=3, width=6, 
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == '' and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.highlight_winner()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.ask_play_again()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.ask_play_again()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != '':
                self.winning_combination = condition
                return True
        return False

    def highlight_winner(self):
        pass
       

    def ask_play_again(self):
        pass


    def reset_board(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

