from enum import Enum


class ChessPieceEnum(Enum):
    PAWN = ''
    KNIGHT = 'C'
    BISHOP = 'B'
    ROOK = 'T'
    QUEEN = 'D'
    KING = 'R'

class ColorEnum(Enum):
    BLACK = 0
    WHITE = 1

class ChessObject:
    def __init__(self, x: int, y: int, width: float, height: float, board_coordinate: tuple[int, int]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.board_coordinate = board_coordinate

class Square(ChessObject):
    def __init__(self, x: int, y: int, width: float, height: float, board_coordinate: tuple[int, int]):
        super().__init__(x,y,width,height, board_coordinate)

class ChessPiece(ChessObject):
    def __init__(
        self, 
        type: ChessPieceEnum, 
        color: ColorEnum, 
        x: int, 
        y: int, 
        width: float, 
        height: float, 
        board_coordinate: tuple[int, int]
    ):
        super().__init__(x,y,width,height, board_coordinate)
        self.type = type
        self.color = color
