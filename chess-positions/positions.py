from chesspiece import ChessPiece, ChessPieceEnum, ColorEnum
from positionbuilder import PositionBuilder
from utils import get_chess_board_size, get_coordinate, get_notation


def get_positions_of(chess_piece: ChessPiece) -> list[tuple[int, int]]:
    x,y = chess_piece.coordinate
    chess_board_size = get_chess_board_size()
    position_builder = PositionBuilder((x,y), chess_board_size)
    match chess_piece.type:
        case ChessPieceEnum.PAWN:
            if chess_piece.color == ColorEnum.WHITE:
                position_builder.up()
                if y == 6: position_builder.up(2)
            else:
                position_builder.down()
                if y == 1: position_builder.down(2)
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
    chess_piece = ChessPiece(ChessPieceEnum.PAWN, get_coordinate('a7'), ColorEnum.WHITE)
    positions = get_positions_of(chess_piece)
    positions_notations = list(map(lambda coordinate: get_notation(coordinate[0], coordinate[1]), positions))
    print(positions)
    print(positions_notations)
