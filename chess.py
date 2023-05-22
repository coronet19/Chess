import os     # spooky line frfr

board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]

# test

pieces = ("WP", "WR", "WN", "WB", "WK", "WQ", "BP", "BR", "BN", "BB", "BK", "BQ")
white_pieces = ("WP", "WR", "WN", "WB", "WK", "WQ")
black_pieces = ("BP", "BR", "BN", "BB", "BK", "BQ")
white_en_passant_list = []
black_en_passant_list = []
error_list = []
move_repetition = []
castle_methods = ("O-O-O", "long castle", "O-O", "short castle")
white_short_castle = True
white_long_castle = True
black_short_castle = True
black_long_castle = True
turn = "white"


#
#
#   Piece Movement
#
#


def rook_moveset(move):
    if not is_killable(move):
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    if move[0] == move[-2]:
        start = reverse_int_index(move[1])
        end = reverse_int_index(move[-1])
        if abs(start - end) == 1:
            return True
        if start > end:
            temp = start
            start = end
            end = temp
        for i in range(start + 1, end):
            if board[i][reverse_alpha_index(move[0])] in pieces:
                error_list.append("Invalid Move: Piece Collision Occurance")
                return False
        return True
    elif move[1] == move[-1]:
        start_rank = reverse_int_index(move[1])
        start = reverse_alpha_index(move[0])
        end = reverse_alpha_index(move[-2])
        if abs(start - end) == 1:
            return True
        if start > end:
            temp = start
            start = end
            end = temp
        for i in range(start + 1, end):
            print(i)
            if board[start_rank][i] in pieces:
                error_list.append("Invalid Move: Piece Collision Occurance")
                return False
        return True
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def bishop_moveset(move):
    if is_killable(move) is False:
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    else:
        error_list.append("is killable")
        start = reverse_alpha_index(move[0])
        end = reverse_alpha_index(move[-2])
        row_start = reverse_int_index(move[1])
        row_end = reverse_int_index(move[-1])

        if abs(start - end) != abs(row_start - row_end):
            error_list.append("Invalid Move: Move Not In Valid Piece Moveset")
            return False

        if start > end:
            temp = start
            start = end
            end = temp

        for i in range(start + 1, end):
            if row_start < row_end:
                temp = row_start
                row_start = row_end
                row_end = temp
            if board[row_start - 1][i] in pieces:
                error_list.append("Invalid Move: Piece Collision Detected")
                return False
            row_start -= 1
            continue
        return True


def knight_moveset(move):
    if is_killable(move) is False:
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    if abs(int(move[1]) - int(move[-1])) == 2:
        if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
            return True
    elif abs(int(move[1]) - int(move[-1])) == 1:
        if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 2:
            return True
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def king_moveset(move):
    if is_killable(move) is False:
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) <= 1:
        if abs(int(move[1]) - int(move[-1])) <= 1:
            return True
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def white_pawn_moveset(move):
    if get_piece(move[-2:]) in pieces:
        if int(move[-1]) - int(move[1]) == 1:
            if is_killable(move):
                if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
                    return True
            if move[0] == move[-2]:
                error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
                return False
    elif get_piece(move[-2:]) not in pieces:
        if int(move[-1]) - int(move[1]) == 1:
            if get_piece(move[-2:]) in black_en_passant_list:
                if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
                    board[3][reverse_alpha_index(move[-2])] = "  "
                    return True
            elif move[0] == move[-2]:
                return True
        elif int(move[1]) == 2 and int(move[-1]) == 4:
            if move[0] == move[-2]:
                if board[5][reverse_alpha_index(move[0])] not in pieces:
                    white_en_passant_list.append(board[5][reverse_alpha_index(move[0])])
                    return True
                else:
                    error_list.append("Invalid Move: Piece Collision Detected")
                    return False
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def black_pawn_moveset(move):
    if get_piece(move[-2:]) in pieces:
        if int(move[1]) - int(move[-1]) == 1:
            if is_killable(move):
                if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
                    return True
            if move[0] == move[-2]:
                error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
                return False
    elif get_piece(move[-2:]) not in pieces:
        if int(move[1]) - int(move[-1]) == 1:
            if get_piece(move[-2:]) in white_en_passant_list:
                if abs(reverse_alpha_index(move[-2]) - reverse_alpha_index(move[0])) == 1:
                    board[4][reverse_alpha_index(move[-2])] = "  "
                    return True
            elif move[0] == move[-2]:
                return True
        elif int(move[1]) == 7 and int(move[-1]) == 5:
            if move[0] == move[-2]:
                if board[2][reverse_alpha_index(move[0])] not in pieces:
                    black_en_passant_list.append(board[2][reverse_alpha_index(move[0])])
                    return True
                else:
                    error_list.append("Invalid Move: Piece Collision Detected")
                    return False
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def castle_availability(move, turn):
    move = str(move).upper()
    if turn == "white":
        if move in ["O-O-O", "LONG CASTLE"]:
            if white_long_castle is True and board[7][:5] == ["WR", "  ", "  ", "  ", "WK"]:
                return True
        elif move in ["O-O", "SHORT CASTLE"]:
            if white_short_castle is True and board[7][4:] == ["WK", "  ", "  ", "WR"]:
                return True
    elif turn == "black":
        if move in ["O-O-O", "LONG CASTLE"]:
            if black_long_castle is True and board[0][:5] == ["BR", "  ", "  ", "  ", "BK"]:
                return True
        elif move in ["O-O", "SHORT CASTLE"]:
            if black_short_castle is True and board[0][4:] == ["BK", "  ", "  ", "BR"]:
                return True
    return False


#
#
#   Utility Functions
#
#

# converts file to a board index
def reverse_alpha_index(letter):
    return ord(letter) - 65

# converts tile rank to a board parent index
def reverse_int_index(number):
    return abs(int(number) - 8)

# gets the piece on a tile
def get_piece(piece):
    return board[reverse_int_index(int(piece[1]))][reverse_alpha_index(piece[0])]

# checks color of both pieces, returns false if equal
def is_killable(move):
    if get_piece(move[:2]) in white_pieces:
        if get_piece(move[-2:]) not in white_pieces:
            return True
    elif get_piece(move[:2]) in black_pieces:
        if get_piece(move[-2:]) not in black_pieces:
            return True
    return False

# checks movesets of pieces
def is_valid(move, turn):
    global error_list
    piece = get_piece(move[:2])
    if turn == "white":
        if piece == "WR":
            return rook_moveset(move)
        elif piece == "WB":
            return bishop_moveset(move)
        elif piece == "WN":
            return knight_moveset(move)
        elif piece == "WQ":
            if rook_moveset(move) is True or bishop_moveset(move) is True:
                error_list = []
                return True
            else:
                if "Invalid Move: Piece In Intended Location Is Not Killable" in error_list:
                    error_list = ["Invalid Move: Piece In Intended Location Is Not Killable"]
                elif "Invalid Move: Piece Collision Detected" in error_list:
                    error_list = ["Invalid Move: Piece Collision Detected"]
                elif "Invalid Move: Intended Location Not In Valid Piece Moveset" in error_list:
                    error_list = ["Invalid Move: Intended Location Not In Valid Piece Moveset"]
        elif piece == "WK":
            return king_moveset(move)
        elif piece == "WP":
            return white_pawn_moveset(move)
    elif turn is "black":
        if piece == "BR":
            return rook_moveset(move)
        elif piece == "BB":
            return bishop_moveset(move)
        elif piece == "BN":
            return knight_moveset(move)
        elif piece == "BQ":
            if rook_moveset(move) is True or bishop_moveset(move) is True:
                error_list = []
                return True
        elif piece == "BK":
            return king_moveset(move)
        elif piece == "BP":
            return black_pawn_moveset(move)
    return False

def pawn_promotion():
    valid_promotions = ["rook", "knight", "bishop", "queen"]
    skip = False
    for key, tile in enumerate(board[0]):
        if tile == "WP":
            while True:
                os.system("clear")
                print_board(turn)
                promotion = input("What Piece Do You Want To Promote To?\nRook, Knight, Bishop, or Queen? ")
                if promotion.strip().lower() in valid_promotions:
                    board[0][key] = f"W{promotion[0].upper()}"
                    skip = True
                    break

    if skip is False:
        for key, tile in enumerate(board[7]):
            if tile == "BP":
                while True:
                    os.system("clear")
                    print_board(turn)
                    promotion = input("What Piece Do You Want To Promote To?\nRook, Knight, Bishop, or Queen? ")
                    if promotion.lower().strip() in valid_promotions:
                        board[7][key] = f"B{promotion[0].upper()}"
                        break


def castle(move, turn):
    if turn == "white":
        if move in ["O-O", "SHORT CASTLE"]:
            board[7][4:] = ["  ", "WR", "WK", "  "]
        elif move in ["O-O-O", "LONG CASTLE"]:
            board[7][:5] = ["  ", "  ", "WK", "WR", "  "]
    elif turn == "black":
        if move in ["O-O", "SHORT CASTLE"]:
            board[0][4:] = ["  ", "BR", "BK", "  "]
        elif move in ["O-O-O", "LONG CASTLE"]:
            board[0][:5] = ["  ", "  ", "BK", "BR", "  "]


def repetition_checker():
    if len(move_repetition) > 8:
        if move_repetition[:4] == move_repetition[4:8]:
            if move_repetition[8] == move_repetition[0]:
                return True
        move_repetition.pop(0)


def update_castle_methods(move, turn):
    global white_short_castle
    global white_long_castle
    global black_short_castle
    global black_long_castle
    piece = get_piece(move[:2])
    if turn == "white":
        if white_short_castle is False and white_long_castle is False:
            return
        if piece == "WK":
            white_short_castle = False
            white_long_castle = False
            return
        elif piece == "WR":
            if move[0] == "A":
                white_long_castle = False
                return
            elif move[0] == "H":
                white_short_castle = False
                return
    elif turn == "black":
        if black_short_castle is False and black_long_castle is False:
            return
        if piece == "WK":
            black_short_castle = False
            black_long_castle = False
            return
        elif piece == "WR":
            if move[0] == "A":
                black_long_castle = False
                return
            elif move[0] == "H":
                black_short_castle = False
                return


# updates displayed board
def update_board(move, turn):
    global error_list
    error_list = []
    # updates castling availability
    if get_piece(move[:2]) in ["WR", "WK", "BR", "BK"]:
        update_castle_methods(move, turn)
    #actually moves the pieces and updates the board
    board[reverse_int_index(move[-1])][reverse_alpha_index(move[-2])] = get_piece(move[:2])
    board[reverse_int_index(move[1])][reverse_alpha_index(move[0])] = "  "


# prints the board with notation
# for black,
def print_board(turn):
    if turn == "white":
        count = 9
        for row in board:
            count -= 1
            print(str(count) + "  ", end="")
            for tile in row:
                if tile == "":
                    print("  ", end="")
                print(tile + " ", end="")
            if board.index(row) < 7:
                print("")
        print("\n   A  B  C  D  E  F  G  H")
    else:
        reverse_board = [
            board[7][::-1],
            board[6][::-1],
            board[5][::-1],
            board[4][::-1],
            board[3][::-1],
            board[2][::-1],
            board[1][::-1],
            board[0][::-1]
            ]
        count = 0
        for row in reverse_board:
            count += 1
            print(str(count), end="  ")
            for tile in row:
                if tile == "":
                    print("  ", end="")
                print(tile, end=" ")
            if reverse_board.index(row) < 7:
                print("")
        print("\n   H  G  F  E  D  C  B  A")


# runs the program
while True:
    try:
        # checks for and promtoes pawns
        pawn_promotion()

        # draws the game if there are 4 repeated moves in a row
        if repetition_checker():
            print("Draw By Repetition")
            break

        os.system("clear")

        print_board(turn)

        # prints errors from previous move
        if error_list:
            for item in error_list:
                print(item)
            error_list = []

        # checks if it is whites turn
        if turn == "white":
            move = input("White To Move: ").upper().strip()
            white_en_passant_list = []
            if move == "PASS":
                turn = "black"
                continue
            if move == "RESIGN":
                print("Black Wins")
                break

            if move in ["O-O-O", "O-O", "LONG CASTLE", "SHORT CASTLE"]:
                if castle_availability(move, turn) is True:
                    castle(move, turn)
                    turn = "black"
                    continue
                else:
                    error_list.append("Invalid Move: Cannot Castle")

            if get_piece(move[:2]) not in pieces:
                error_list.append("Invalid Move: No Piece Selected")
                continue

            if is_valid(move, turn):
                move_repetition.append(move)
                update_board(move, turn)
                turn = "black"
                continue

        elif turn == "black":
            move = input("Black To Move: ").upper()
            black_en_passant_list = []
            if move == "PASS":
                turn = "white"
                continue
            elif move == "RESIGN":
                print("White Wins")
                break

            if move in ["O-O-O", "O-O", "LONG CASTLE", "SHORT CASTLE"]:
                if castle_availability(move, turn) is True:
                    castle(move, turn)
                    turn = "black"
                    continue
                else:
                    error_list.append("Invalid Move: Cannot Castle")

            if get_piece(move[:2]) not in pieces:
                error_list.append("Invalid Move: No Piece Selected")
                continue

            elif is_valid(move, turn):
                move_repetition.append(move)
                update_board(move, turn)
                turn = "white"
                continue
    except:
        continue
    else:
        continue