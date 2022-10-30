from enum import Enum

from positionbuilder import PositionBuilder
from utils import get_chess_board_size, get_coordinate, get_notation


#  king, rook, bishop, queen, knight, and pawn
class ChessPieceEnum(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

class ChessPiece:
    def __init__(self, type: ChessPieceEnum, coordinate: tuple[int, int]):
        self.type: ChessPieceEnum = type
        self.coordinate: tuple[int, int] = coordinate

def get_position_of(chess_piece: ChessPiece) -> list[tuple[int, int]]:
    x,y = chess_piece.coordinate
    chess_board_size = get_chess_board_size()
    position_builder = PositionBuilder((x,y), chess_board_size)
    match chess_piece.type:
        case ChessPieceEnum.PAWN: 
            position_builder.up()
            if y == 6: position_builder.up(2)
        case ChessPieceEnum.KNIGHT: 
            position_builder\
                .up_left(2, 1)\
                .up_left(1, 2)\
                .up_right(2, 1)\
                .up_right(1, 2)\
                .down_left(2, 1)\
                .down_left(1, 2)\
                .down_right(2, 1)\
                .down_right(1, 2)
        case ChessPieceEnum.BISHOP: 
            position_builder.in_diagonal()
        case ChessPieceEnum.ROOK: 
            position_builder\
                .in_column()\
                .in_row()
        case ChessPieceEnum.QUEEN: 
            position_builder\
                .in_column()\
                .in_row()\
                .in_diagonal()
        case ChessPieceEnum.KING: 
            position_builder\
                .up()\
                .up_left()\
                .up_right()\
                .left()\
                .right()\
                .down()\
                .down_left()\
                .down_right()
    return position_builder.build()

if __name__ == '__main__':
    chess_piece = ChessPiece(ChessPieceEnum.QUEEN, get_coordinate('a8'))
    positions = get_position_of(chess_piece)
    positions_notations = list(map(lambda coordinate: get_notation(coordinate[0], coordinate[1]), positions))
    print(positions)
    print(positions_notations)
