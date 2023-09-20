# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
        Takes input for the next move and updates the board
        """
        while True:
            position = int(input("Your move! Choose a position (1-9): ")) - 1
            if board[position] == ' ':
                board[position] = 'X'
                break
            else:
                print("Invalid move. Try again.")            
                

if __name__ == "__main__":
    game = TicTacToe()
    player = Player()
    print("Initial board:")
    game.print_board()
    
    player.make_move(game.board)
    print("Board after players move:")
    game.print_board()