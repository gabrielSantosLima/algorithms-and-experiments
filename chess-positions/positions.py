from enum import Enum
from utils import get_chess_board_size, get_coordinate, get_notation

#  king, rook, bishop, queen, knight, and pawn
class ChessPiece(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

def get_position_of(chess_piece: ChessPiece, coordinate: tuple[int, int]) -> list[tuple[int, int]]:
    x,y = coordinate
    chess_board_size = get_chess_board_size()
    positions: list[tuple[int, int]] = []
    if chess_piece == ChessPiece.PAWN:
        positions.append((x, y - 1))
        if y == 6: positions.append((x, y - 2))
    elif chess_piece == ChessPiece.KNIGHT:
        if x - 2 >= 0 and y - 1 >= 0: positions.append((x-2, y-1)) 
        if x - 2 >= 0 and y + 1 < chess_board_size: positions.append((x-2, y+1)) 
        if x + 2 < chess_board_size and y - 1 >= 0: positions.append((x+2, y-1)) 
        if x + 2 < chess_board_size and y + 1 < chess_board_size: positions.append((x+2, y+1)) 
       
        if x - 1 >= 0 and y - 2 >= 0: positions.append((x-1, y-2)) 
        if x + 1 < chess_board_size and y - 2 >= 0: positions.append((x+1, y-2)) 
        if x - 1 >= 0 and y + 2 < chess_board_size: positions.append((x-1, y+2)) 
        if x + 1 < chess_board_size and y + 2 < chess_board_size: positions.append((x+1, y+2)) 
    return positions

if __name__ == '__main__':
    positions = get_position_of(ChessPiece.KNIGHT, get_coordinate('d8'))
    positions_notations = list(map(lambda coordinate: get_notation(coordinate[0], coordinate[1]), positions))
    print(positions)
    print(positions_notations)