from chesspiece import ChessObject, ChessPiece, ChessPieceEnum, ColorEnum
from positionbuilder import PositionBuilder
from utils import get_chess_board_size, get_coordinate, get_notation


def get_positions_of(chess_board: list[list[ChessObject]], chess_piece: ChessPiece) -> list[tuple[int, int]]:
    x,y = chess_piece.board_coordinate
    chess_board_size = get_chess_board_size()
    position_builder = PositionBuilder((x,y), chess_board_size, chess_board)
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

def print_board(chess_board: list[list[ChessObject]]):
    for row in range(8):
        for column in range(8):
            el = chess_board[row][column]
            if isinstance(chess_board[row][column], ChessPiece):
                print(el.type.value, end='')
            print(get_notation(el.board_coordinate[0], el.board_coordinate[1]), end=' ')
        print()

if __name__ == '__main__':
    board: list[list[ChessObject]] = []
    
    for row in range(8):
        board.append([])
        for column in range(8):
            board[row].append(ChessObject(row * 10, column * 10, 10, 10, (column, row)))
    
    board[0][0] = ChessPiece(ChessPieceEnum.ROOK, ColorEnum.BLACK, 10, 10, 10, 10, get_coordinate('a8'))
    chess_piece = ChessPiece(
        ChessPieceEnum.BISHOP, 
        ColorEnum.WHITE,
        30,
        30,
        10,
        10,
        get_coordinate('d5')
    )
    board[3][3] = chess_piece
    
    positions = get_positions_of(board, chess_piece)
    positions_notations = list(
        map(lambda coordinate: get_notation(coordinate[0], coordinate[1]), positions)
    )
    print_board(board)
    print(positions, end='')
    print(positions_notations)
