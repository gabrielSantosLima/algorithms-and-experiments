from enum import Enum


class ChessPieceEnum(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

class ColorEnum(Enum):
    BLACK = 0
    WHITE = 1

class ChessPiece:
    def __init__(self, type: ChessPieceEnum, coordinate: tuple[int, int], color: ColorEnum):
        self.type: ChessPieceEnum = type
        self.color: ColorEnum = color
        self.coordinate: tuple[int, int] = coordinate
