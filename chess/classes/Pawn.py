from model.Piece import Piece


class Pawn(Piece):
    def __init__(self, name, color):
        super().__init__(name, color)
        
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        return start_col == end_col and end_row == start_row + 1