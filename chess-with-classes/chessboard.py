from pawn import pawn

class board:
    def __init__(self):
        self.board = [
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎"],
            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
        ]

        self.reference_board = [
            ["▮", "▯", "▮", "▯", "▮", "▯", "▮", "▯"],
            ["▯", "▮", "▯", "▮", "▯", "▮", "▯", "▮"],
            ["▮", "▯", "▮", "▯", "▮", "▯", "▮", "▯"],
            ["▯", "▮", "▯", "▮", "▯", "▮", "▯", "▮"],
            ["▮", "▯", "▮", "▯", "▮", "▯", "▮", "▯"],
            ["▯", "▮", "▯", "▮", "▯", "▮", "▯", "▮"],
            ["▮", "▯", "▮", "▯", "▮", "▯", "▮", "▯"],
            ["▯", "▮", "▯", "▮", "▯", "▮", "▯", "▮"]
        ]

    def assign_classes(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == "♟︎":
                    p = pawn
                    self.board[i][j] = p
                    self.board[i][j].update_moves(self.board)
    
    def print_board(self):
        for a in range(8):
            print("")
            for b in range(8):
                if self.board[a][b] == "":
                    print(self.reference_board[a][b], end = " ")
                else:
                    print(self.board[a][b], end = " ")