# Initial imports
import random
import os
from colorama import init, Fore, Style
import time

init(autoreset=True)


def clearConsole():
    """
    Clears the console screen based on the operating system.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


class WelcomeScreen:
    """
    Manages the initial screen display showing the game rules and the logo.
    """
    LOGO = Fore.CYAN + Style.BRIGHT + r"""

  _____ _         _____             _____
 |_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___
   | | | |/ __|____| |/ _` |/ __|____| |/ _ \ / _ \
   | | | | (_|_____| | (_| | (_|_____| | (_) |  __/
   |_| |_|\___|    |_|\__,_|\___|    |_|\___/ \___|
    """

    RULES = Fore.YELLOW + """
        ====================================
              Welcome to Tic-Tac-Toe!
        ====================================

 Here are the rules:
 1. The board has positions 1-9 starting from top-left and going row-wise.
 2. You are 'X' and the computer is 'O'.
 3. To win, get three of your marks in a row, column, or diagonal.
 4. Input your move as a number between 1 and 9 to place your mark.
 5. If the board fills up without a winner, it's a draw.
 ===================================
    """

    @staticmethod
    def display_logo_and_rules():
        """
        Displays the game logo and rules.
        """
        clearConsole()
        print(WelcomeScreen.LOGO)
        print(WelcomeScreen.RULES)

    @staticmethod
    def get_difficulty_input():
        """
        Gets difficulty level input from the user and validates it.
        """
        valid_difficulties = ['e', 'easy', 'm', 'medium', 'h', 'hard']
        error_message = ""

        while True:
            WelcomeScreen.display_logo_and_rules()
            if error_message:
                print(Fore.RED + error_message + Style.RESET_ALL)
            difficulty = input(Fore.CYAN + "Choose difficulty level -"
                               " Easy (e), Medium (m), Hard (h): \n"
                               + Style.RESET_ALL).lower().strip()
            if difficulty in valid_difficulties:
                return difficulty[0]
            error_message = "Invalid option. Please choose again."

    @staticmethod
    def display():
        """
        Displays the welcome screen and returns the choosen difficulty level.
        """
        return WelcomeScreen.get_difficulty_input()


class TicTacToe:
    """
    A class to represent the TicTacToe game, managing its board and flow.
    """
    def __init__(self, difficulty):
        """
        Initialize the game board and set initial scores.
        """
        self.board = [' ' for _ in range(9)]
        self.player_score = 0
        self.computer_score = 0
        self.difficulty = difficulty

    def display_score(self):
        """Displays the current game's score and difficulty level."""

        difficulty_mapping = {'e': 'Easy', 'm': 'Medium', 'h': 'Hard'}
        difficulty_name = difficulty_mapping.get(self.difficulty, "Unknown")

        print("\nDifficulty Level: " + Fore.CYAN + f"{difficulty_name}")
        print("Current score:")
        print("Player: " + Fore.GREEN + f"{self.player_score}"
              + Style.RESET_ALL + " - " "Computer: "
              + Fore.RED + f"{self.computer_score}")
        print("===========================")

    def print_board(self):
        """Displays the current state of the TicTacToe board with symbols."""
        print(Fore.CYAN + Style.BRIGHT + "        Tic-Tac-Toe  ")
        print(Fore.BLUE + "---------------------------")

        # Display each row of the board with colored symbols for X and O
        for i in range(0, 9, 3):
            row = []
            for j in range(3):
                if self.board[i+j] == 'X':
                    row.append(Fore.GREEN + self.board[i+j] + Style.RESET_ALL)
                elif self.board[i+j] == 'O':
                    row.append(Fore.RED + self.board[i+j] + Style.RESET_ALL)
                else:
                    row.append(self.board[i+j])
            print(f" {i+1} | {i+2} | {i+3} "
                  f"      {row[0]} | {row[1]} | {row[2]} ")
            if i < 6:
                print("---+---+---     ---+---+---")
        print(Fore.BLUE + "---------------------------")

    def check_winner(self, char):
        """
        Check for a winning condition based on the provided symbol.
        """
        # Check rows, columns, and diagonals for win
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == char:
                return True
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == char:
                return True
        if self.board[0] == self.board[4] == self.board[8] == char:
            return True
        if self.board[2] == self.board[4] == self.board[6] == char:
            return True
        return False

    def check_draw(self):
        """
        Check if the game has reached a draw state.
        """
        if ' ' not in self.board:
            self.print_board()
            print("It's a draw!")
            return True
        return False

    def make_and_check_move(self, mover, symbol, win_message,
                            game_instance=None):
        """Make a move and check if it resulted in a win"""
        mover.make_move(self.board, game_instance)
        if self.check_winner(symbol):
            self.print_board()
            print(win_message)
            return True
        return False

    def update_score(self, winner):
        """Update the score based on the winner."""
        if winner == 'Player':
            self.player_score += 1
        elif winner == 'Computer':
            self.computer_score += 1

    def play_game(self):
        """
        Main game loop that brings all the functionalities together.
        """

        player = Player()
        computer = Computer(difficulty, self.check_winner)
        game_count = 0

        while True:
            self.board = [' ' for _ in range(9)]

            # Game round loop
            while True:
                self.display_full_board()

                # Player's turn
                if self.make_and_check_move(player, 'X', "Player wins!\n,",
                                            self):
                    clearConsole()
                    self.update_score('Player')
                    self.display_score()
                    self.print_board()
                    print(Fore.GREEN + "Player wins!\n" + Style.RESET_ALL)
                    time.sleep(2)
                    clearConsole()
                    break

                if self.check_draw():
                    self.display_full_board()
                    print("It's a draw!")
                    time.sleep(2)
                    clearConsole()
                    break

                # Computer's turn
                self.display_full_board()
                print("Computer is thinking", end="")
                for _ in range(3):
                    time.sleep(0.4)
                    print(".", end="", flush=True)
                print()
                time.sleep(1.3)

                if self.make_and_check_move(computer, 'O', "Computer wins"):
                    clearConsole()
                    self.update_score('Computer')
                    self.display_score()
                    self.print_board()
                    print(Fore.RED + "Computer wins" + Style.RESET_ALL)
                    time.sleep(2)
                    clearConsole()
                    break

            # Check for end-of-session after 2 rounds
            game_count += 1
            if game_count == 2:
                self.display_full_board()
                print("You've played 2 games!")

                # Post-session choices
                while True:
                    if self.difficulty == 'h':
                        choice = input("Continue playing or exit?"
                                       " (c/e):\n").lower().strip()
                    else:
                        choice = input("Continue playing, increase difficulty,"
                                       " or exit? (c/i/e):\n").lower().strip()

                    valid_choices = (['c', 'i', 'e']
                                     if self.difficulty != 'h'
                                     else ['c', 'e'])

                    if choice in valid_choices:
                        game_count = 0
                        break
                    self.display_full_board()

                    if self.difficulty == 'h':
                        print(Fore.RED + "Invalid input. Please choose 'c'"
                              "(continue) or 'e'(exit)." + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Invalid input. Please choose 'c'"
                              "(continue), 'i'(increase),"
                              " or 'e'(exit)." + Style.RESET_ALL)

                if choice == 'e':
                    return
                elif choice == 'i':
                    # Adjust difficulty
                    if self.difficulty == 'e':
                        self.difficulty = 'm'
                    elif self.difficulty == 'm':
                        self.difficulty = 'h'
                        computer = Computer(self.difficulty, self.check_winner)
                    game_count = 0

    def display_full_board(self):
        """Display score, difficulty and the board"""
        clearConsole()
        self.display_score()
        self.print_board()


class Player:
    """Handles player actions."""
    def make_move(self, board, game_instance):
        """
        Prompts the player to make a move and updates the board accordingly.
        """
        while True:
            try:
                position = int(input(
                    "Your move! Choose a position (1-9): \n"
                    )) - 1
                # Check if the input position is within the valid range
                if 0 <= position < 9:
                    # Check if the chosen position is unoccupied
                    if board[position] == ' ':
                        board[position] = 'X'
                        break
                    else:
                        game_instance.display_full_board()
                        print(Fore.RED + "Invalid move."
                              " Try again." + Style.RESET_ALL)
                else:
                    game_instance.display_full_board()
                    print(Fore.RED + "Invalid position. Choose a"
                          " number between 1 and 9." + Style.RESET_ALL)
            # Handle non-integer inputs
            except ValueError:
                game_instance.display_full_board()
                print(Fore.RED + "Please enter a number"
                      " between 1 and 9." + Style.RESET_ALL)


class Computer:
    """
    handles computer's decisions and actions in the game.
    """
    def __init__(self, difficulty, check_winner_func):
        """
        Initialize the computer player with the specified difficulty.
        """
        self.difficulty = difficulty
        self.check_winner_func = check_winner_func

    def find_winning_move(self, board, symbol):
        """
        Find a move for the computer that would result in a win.
        """
        for i in range(9):
            if board[i] == ' ':
                board[i] = symbol
                if self.check_winner_func(symbol):
                    return True
                # Reset the board to its original state
                board[i] = ' '
        return False

    def find_blocking_move(self, board):
        """
        Find a move that blocks the player from winning on the next turn.
        """
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                if self.check_winner_func('X'):
                    board[i] = 'O'
                    return True
                board[i] = ' '
        return False

    def make_move(self, board, game_instance=None):
        """
        Make a move based on the difficulty setting and update the board.
        """
        # Hard diff.: comp tries to win, then blocks player from winning
        if self.difficulty == 'h':
            if self.find_winning_move(board, 'O'):
                return
            if self.find_blocking_move(board):
                return

        # Medium diff.: computer only tries to win
        elif self.difficulty == 'm':
            if self.find_winning_move(board, 'O'):
                return

        # Easy diff.: computer only makes random moves
        available_positions = [i for i, x in enumerate(board) if x == ' ']
        if available_positions:
            position = random.choice(available_positions)
            board[position] = 'O'


if __name__ == "__main__":
    """
    Main game loop
    """
    while True:
        # Clear any previous console output for a fresh game start
        clearConsole()

        # Display the welcome screen and retrieve the chosen difficulty
        difficulty = WelcomeScreen.display()

        # Clear console again for the game
        clearConsole()

        # Initialize the game instance with chosen difficulty
        game = TicTacToe(difficulty)

        # Start the game
        game.play_game()

        # Display the board and thank the player for playing
        game.display_full_board()
        print(Fore.YELLOW + "\nThank you for playing"
              " Tic-Tac-Toe!" + Style.RESET_ALL)

        # Ask the player if they wish to play again
        choice = input("Play again? (Yes/No): ").lower().strip()

        while choice not in ['yes', 'y', 'no', 'n']:
            game.display_full_board()
            print(Fore.RED + "Invalid input. Please type 'Yes'"
                  " or 'No'." + Style.RESET_ALL)
            choice = input("Play again? (Yes/No): ").lower().strip()
        if choice in ['no', 'n']:
            print(Fore.GREEN + "Goodbye! Hope to see you"
                  " again soon." + Style.RESET_ALL)
            break
