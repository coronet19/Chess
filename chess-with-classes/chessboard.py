from dataclasses import dataclass

@dataclass
class chessBoard:
    #board: list = []
    def __post_init__(self):
        self.board = [
            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
            ["♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
        ]
    
    def printBoard(self):
        for a in range(8):
            for b in range(8):
                print(self.board[a][b])#, end = " ")