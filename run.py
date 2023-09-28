# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import os
from colorama import init, Fore, Style
import time

init(autoreset=True)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


class WelcomeScreen:
    @staticmethod
    def display():
        print(Fore.CYAN + Style.BRIGHT + r"""
  _______          ______               ______
 /_  __(_)____    /_  __/___ ______    /_  __/___  ___
  / / / / ___/_____/ / / __ `/ ___/_____/ / / __ \/ _ \\
 / / / / /__/_____/ / / /_/ / /__/_____/ / / /_/ /  __/
/_/ /_/\___/     /_/  \__,_/\___/     /_/  \____/\___/
        """)
        print(Fore.YELLOW + "===================================")
        print(Fore.YELLOW + "     Welcome to Tic-Tac-Toe!")
        print(Fore.YELLOW + "===================================")
        print("Here are the rules:")
        print("1. The board has positions 1-9 starting from top-left"
              " and going row-wise.")
        print("2. You are 'X' and the computer is 'O'.")
        print("3. To win, get three of your marks in a row, column,"
              " or diagonal.")
        print("4. Input your move as a number between"
              " 1 and 9 to place your mark.")
        print("5. If the board fills up without a winner, it's a draw.")
        print("===================================")

        difficulty = input("Choose difficulty level - Easy (e), Medium (m),"
                           " Hard (h): \n").lower()
        while difficulty not in ['e', 'm', 'h']:
            print("Invalid option. Please choose again.")
            difficulty = input("Choose difficulty level - Easy (e),"
                               " Medium (m), Hard (h): \n").lower()
        return difficulty


class TicTacToe:
    """
    Manages the game board and flow.
    """
    def __init__(self, difficulty):
        """
        Initialize an empty game board.
        """
        self.board = [' ' for _ in range(9)]
        self.player_score = 0
        self.computer_score = 0
        self.difficulty = difficulty

    def display_score(self):
        """Displays the current score and difficulty."""

        difficulty_mapping = {'e': 'Easy', 'm': 'Medium', 'h': 'Hard'}
        difficulty_name = difficulty_mapping.get(self.difficulty, "Unknown")

        print(f"Difficulty Level: {difficulty_name}")
        print(f"Current Score: Player {self.player_score} -"
              " Computer {self.computer_score}")
        print("===================================")

    def print_board(self):
        """Prints the game board."""
        print(Fore.CYAN + Style.BRIGHT + "        Tic-Tac-Toe  ")
        print(Fore.BLUE + "---------------------------")
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
        Check for a winning condition for 'char' in game.
        """
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
        """Check for a draw"""
        if ' ' not in self.board:
            self.print_board()
            print("It's a draw!")
            return True
        return False

    def make_and_check_move(self, mover, symbol, win_message):
        """Make a move and check if it resulted in a win"""
        mover.make_move(self.board)
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

            while True:
                clearConsole()
                self.display_score()
                self.print_board()

                if self.make_and_check_move(player, 'X', "Player wins!\n"):
                    clearConsole()
                    self.update_score('Player')
                    self.display_score()
                    self.print_board()
                    print("Player wins!\n")
                    time.sleep(2)
                    clearConsole()
                    break

                if self.check_draw():
                    clearConsole()
                    self.display_score()
                    self.print_board()
                    print("It's a draw!")
                    time.sleep(2)
                    clearConsole()
                    break

                # Computers move
                clearConsole()
                self.display_score()
                self.print_board()
                print("Computer is thinking...")
                time.sleep(1.3)

                if self.make_and_check_move(computer, 'O', "Computer wins"):
                    clearConsole()
                    self.update_score('Computer')
                    self.display_score()
                    self.print_board()
                    print("Computer wins")
                    time.sleep(2)
                    clearConsole()
                    break

                if self.check_draw():
                    clearConsole()
                    self.display_score()
                    self.print_board()
                    print("It's a draw!")
                    time.sleep(2)
                    clearConsole()
                    break

            game_count += 1
            if game_count == 2:
                clearConsole()
                self.display_score()
                self.print_board()

                print("You've played 2 games!")
                if self.difficulty == 'h':
                    while True:
                        choice = input("Do you want to keep playing?"
                                       " (y/n):\n").lower()
                        if choice in ['y', 'n']:
                            break
                        print("Invalid input. Please choose 'y' or 'n'.")
                    if choice == 'n':
                        return  # exit the game
                else:
                    while True:
                        choice = input("Do you want to increase"
                                       " difficulty or exit? (i/e).\n")
                        if choice in ['i', 'e']:
                            break
                        print("Invalid input. Please choose 'i'(increase)"
                              " or 'e'(exit).")
                    if choice == 'e':
                        return  # exit the game
                    elif choice == 'i':
                        if self.difficulty == 'e':
                            self.difficulty = 'm'
                        elif self.difficulty == 'm':
                            self.difficulty = 'h'
                        computer = Computer(self.difficulty, self.check_winner)
                game_count = 0


class Player:
    """Handles player actions."""
    def make_move(self, board):
        """
        Takes input for the next move and updates the board.
        """
        while True:
            try:
                position = int(input(
                    "Your move! Choose a position (1-9): \n"
                    )) - 1
                if 0 <= position < 9:
                    if board[position] == ' ':
                        board[position] = 'X'
                        break
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Invalid position. Choose a number between 1 and 9.")
            except ValueError:
                print("Please enter a number between 1 and 9.")


class Computer:
    def __init__(self, difficulty, check_winner_func):
        self.difficulty = difficulty
        self.check_winner_func = check_winner_func

    def find_winning_move(self, board, symbol):
        for i in range(9):
            if board[i] == ' ':
                board[i] = symbol
                if self.check_winner_func(symbol):
                    return True
                board[i] = ' '
        return False

    def find_blocking_move(self, board):
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                if self.check_winner_func('X'):
                    board[i] = 'O'
                    return True
                board[i] = ' '
        return False

    def make_move(self, board):
        if self.difficulty == 'h':
            if self.find_winning_move(board, 'O'):
                return
            if self.find_blocking_move(board):
                return

        elif self.difficulty == 'm':
            if self.find_winning_move(board, 'O'):
                return

        available_positions = [i for i, x in enumerate(board) if x == ' ']
        if available_positions:
            position = random.choice(available_positions)
            board[position] = 'O'


if __name__ == "__main__":
    while True:
        clearConsole()
        difficulty = WelcomeScreen.display()
        clearConsole()
        game = TicTacToe(difficulty)
        game.play_game()

        print("\nThank you for playing Tic-Tac-Toe!")
        choice = input("Would you like to play again? (y/n): \n").lower()
        if choice == 'n':
            break
