from chessboard import board as cb
from pawn import pawn


class chess():
    def __init__(self):
        self.black_pieces = ["♖", "♘", "♗", "♕", "♔", "♙"]
        self.white_pieces = ["♜", "♞", "♝", "♛", "♚", "  ♟︎"]
                

    def run(self): 
        print(self.black_pieces)
        board = cb
        board.assign_classes

        winner = None
        while winner is None:
            break
        board.print_board()
        print("hello")

if __name__ == '__main__':
    game = chess
    game.run