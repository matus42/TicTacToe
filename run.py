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

if __name__ == "__main__":
    game = TicTacToe()
    print("Testing print_board method:")
    game.print_board()