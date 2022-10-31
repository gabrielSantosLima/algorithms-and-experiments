from chesspiece import ChessObject, ChessPiece


class PositionBuilder:
    def __init__(self, coordinate: tuple[int, int], size:int, chess_board: list[list[ChessObject]]):
        self.coordinate: tuple[int, int] = coordinate
        self.positions: list[tuple[int, int]] = []
        self.size: int = size
        self.chess_board = chess_board

    def __position_has_chess_piece(self, x: int, y: int):
        return isinstance(self.chess_board[y][x], ChessPiece)

    def __add_position(self, x: int,y: int):
        self.positions.append((x,y))

    def in_row(self) -> 'PositionBuilder':
        x, y = self.coordinate
        current_x, current_y = 0, y
        while current_x < self.size:
            if current_x != x: 
                self.__add_position(current_x, current_y)
            current_x += 1
        return self
    
    def in_column(self) -> 'PositionBuilder':
        x, y = self.coordinate
        current_x, current_y = x, 0
        while current_y < self.size:
            if current_y != y: self.__add_position(current_x, current_y)
            current_y += 1
        return self
    
    def in_diagonal(self) -> 'PositionBuilder':
        x, y = self.coordinate
        current_x, current_y = self.coordinate
        while current_x - 1 >= 0 and current_y - 1 >= 0:
            current_x -= 1
            current_y -= 1
        while 0 <= current_x < self.size and 0 <= current_y < self.size:
            if current_x != x and current_y != y: 
                self.__add_position(current_x, current_y)
            current_x += 1
            current_y += 1
        current_x, current_y = x, y
        while current_x + 1 < self.size and current_y - 1 >= 0:
            current_x += 1
            current_y -= 1
        while 0 <= current_x < self.size and 0 <= current_y < self.size:
            if current_x != x and current_y != y: 
                self.__add_position(current_x, current_y)
            current_x -= 1
            current_y += 1
        return self
    
    def up(self, squares = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if y - squares >= 0 and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x,y - squares)
        return self
    
    def up_left(self, squares_x = 1, squares_y = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if y - squares_y >= 0 and x - squares_x >= 0 and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x - squares_x,y - squares_y)
        return self
    
    def up_right(self, squares_x = 1, squares_y = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if y - squares_y >= 0 and x + squares_x < self.size and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x + squares_x,y - squares_y)
        return self
    
    def left(self, squares = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if x - squares >= 0 and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x - squares,y)
        return self
    
    def right(self, squares = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if x + squares < self.size and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x + squares,y)
        return self
    
    def down(self, squares = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if y + squares < self.size and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x,y + squares)
        return self
    
    def down_left(self, squares_x = 1, squares_y = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if y + squares_y < self.size and x - squares_x >= 0 and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x - squares_x,y + squares_y)
        return self
    
    def down_right(self, squares_x = 1, squares_y = 1) -> 'PositionBuilder':
        x,y = self.coordinate
        if y + squares_y < self.size and x + squares_x < self.size and not self.__position_has_chess_piece(x, y): 
            self.__add_position(x + squares_x,y + squares_y)
        return self
    
    def build(self) -> list[tuple[int, int]]:
        return self.positions
