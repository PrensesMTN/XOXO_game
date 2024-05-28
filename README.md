# XOXO_game (Tic Tac Toe)
My version of XOXO game
This project is a simple Tic Tac Toe (XOXO) game developed using Python and Tkinter. Players take turns playing X and O on a 3x3 grid and aim to win by aligning three marks in a row.

## Features

- Two-player Tic Tac Toe game on a 3x3 grid
- Highlights winning combination
- Option to play again after the game ends
- Simple and user-friendly interface

## Requirements

- Python 3.x
- Tkinter (comes with Python)
```markdown 
sometimes not so you basically install tkinter package using pip 
write " pip install tkinter " in your terminal or command prompt.
```
## Installation and Running

1. Clone or download this project to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the following command to start the game:

   ```py
   python tic_tac_toe.py
   ```

## Code Explanation

### Main Class: TicTacToe

#### `__init__(self, root)`

- Initializes and starts the game window.
- Initializes the game board and buttons.

#### `create_buttons(self)`

- Creates and places buttons on a 3x3 grid.

#### `on_button_click(self, index)`

- Handles button click events.
- Marks the current player's move on the board and checks for a winner.
- Provides an option to play again at the end of the game.

#### `check_winner(self)`

- Checks for winning combinations on the game board.

#### `highlight_winner(self)`

- Highlights the winning combination.

#### `ask_play_again(self)`

- Asks the player if they want to play again.

#### `reset_board(self)`

- Resets the game board and starts a new game.

### Main Program

- Initializes the window and runs the game.


## Contributing

1. Fork this project.
2. Create a new branch (`feature-branch`).
3. Make your changes and commit them.
4. Push to your branch.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
