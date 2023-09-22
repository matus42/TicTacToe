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
        self.player_score = 0
        self.computer_score = 0
        
    def print_board(self):
        """
        Prints the current state of the game board.
        """
        for i in range (0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            
            
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
        if ' ' not in self.board:
            self.print_board()
            print("It's a draw!")
            return True
        return False
    
    def make_and_check_move(self, mover, symbol, win_message):
        mover.make_move(self.board)
        if self.check_winner(symbol):
            self.print_board()
            print(win_message)
            return True
        return False
    
    def update_score(self, winner):
        if winner == 'Player':
            self.player_score += 1
        elif winner == 'Computer':
            self.computer_score += 1
                
    
    
    def play_game(self):
        """
        Main game loop that brings all the functionalities togethe.
        """
        player = Player()
        computer = Computer()
        
        while True:
            self.board = [' ' for _ in range(9)]
        
            while True:
                self.print_board()
                
                if self.make_and_check_move(player, 'X', "Player wins!"):
                    self.update_score('Player')
                    break
                if self.check_draw():
                    break
                    
                print("Computer made its move.")
            
                if self.make_and_check_move(computer, 'O', "Computer wins"):
                    self.update_score('Computer')
                    break
                if self.check_draw():
                    break
            
            print(f"Current Score: Player {self.player_score} - Computer {self.computer_score}")             
                   
            
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
    game.play_game()      
    
    