import tkinter as tk
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)



def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def bot_move(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if check_winner(board) == player:
                    return
                board[i][j] = " "
    opponent = "X" if player == "O" else "O"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent
                if check_winner(board) == opponent:
                    board[i][j] = player
                    return
                board[i][j] = " "
                
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_spots:
        row, col = random.choice(empty_spots)
        board[row][col] = player

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = check_winner(self.board)
            if winner:
                self.show_winner(winner)
            elif is_board_full(self.board):
                self.show_winner("Tie")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.root.after(500, self.bot_move)

    def bot_move(self):
       # bot_move(self.board, self.current_player)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != self.buttons[i][j].cget('text'):
                    self.buttons[i][j].config(text=self.board[i][j])
        winner = check_winner(self.board)
        if winner:
            self.show_winner(winner)
        elif is_board_full(self.board):
            self.show_winner("Tie")
        self.current_player = "X"

    def show_winner(self, winner):
        result = "It's a tie!" if winner == "Tie" else f"Player {winner} wins!"
        result_label = tk.Label(self.root, text=result, font=('normal', 20))
        result_label.grid(row=3, column=0, columnspan=3)
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
