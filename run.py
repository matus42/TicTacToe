# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

class TicTacToe:
    """
    Manages the game board and flow.
    """
    def __init__(self):
        """
        Initialize an empty game board.
        """
        self.board = [' ' for _ in range(9)]
        
    def print_board(self):
        """
        Prints the current state of the game board.
        """
        for i in range (0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            
class Player:
    """Handles player actions."""
    def make_move(self, board):
        """
        Takes input for the next move and updates the board.
        """
        while True:
            position = int(input("Your move! Choose a position (1-9): ")) - 1
            if board[position] == ' ':
                board[position] = 'X'
                break
            else:
                print("Invalid move. Try again.") 
                
                
class Computer:
    """Handles computer actions"""
    
    def make_move(self, board):
        """
        Makes a random move for the computer and updates the board.
        """
        position = random.choice([i for i, x in enumerate(board) if x == ' '])
        board[position] = 'O'                           
                

if __name__ == "__main__":
    game = TicTacToe()
    player = Player()
    computer = Computer()
    print("Initial board:")
    game.print_board()
    
    #test player move
    player.make_move(game.board)
    print("Board after players move:")
    game.print_board()
    
    #test computers make_move method
    print("Computer's turn:")
    computer.make_move(game.board)
    
    print("Board after computer's move:")
    game.print_board()
    
    