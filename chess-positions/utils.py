BLACK_COLOR = 0
WHITE_COLOR = 1
CHESS_BOARD_SIZE = 8

def column_notations() -> list[str]:
    return list("abcdefgh")

def row_notations() -> list[str]:
    return list("12345678")

def get_chess_board_size():
    return CHESS_BOARD_SIZE

# Returns the white perspective notation
def get_notation(x: int, y:int) -> str:
    chess_board_size = get_chess_board_size()
    columns = column_notations()
    rows = row_notations()
    rows.reverse()
    if y >= chess_board_size or y < 0 or x >= chess_board_size or x < 0:
        return "unknown"
    return f"{columns[x]}{rows[y]}"

# Returns the white perspective coordinate
def get_coordinate(notation: str) -> tuple[int, int]:
    column, row = notation
    if column not in column_notations() or row not in row_notations(): return (-1,-1)
    x = column_notations().index(column)
    rows = row_notations()
    rows.reverse()
    y = rows.index(row)
    return (x, y)

# Returns the numeric chess board
def get_numeric_chess_board(right_left_perspective = False) -> list[list[int]]:
    chess_board: list[list[int]] = []
    chess_board_size = get_chess_board_size()
    current_color = BLACK_COLOR if right_left_perspective else WHITE_COLOR
    
    for row in range(chess_board_size):
        chess_board.append([])
        for _ in range(chess_board_size):
            chess_board[row].append(current_color)
            current_color = BLACK_COLOR if current_color == WHITE_COLOR else WHITE_COLOR
        current_color = BLACK_COLOR if current_color == WHITE_COLOR else WHITE_COLOR

    return chess_board 

# Returns the notated chess board
def get_notated_chess_board() -> list[list[str]]:
    chess_board: list[list[str]] = []
    chess_board_size = get_chess_board_size()
    
    for row in range(chess_board_size):
        chess_board.append([])
        for column in range(chess_board_size):
            chess_board[row].append(get_notation(column, row))

    return chess_board 