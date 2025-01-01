from model.Piece import Piece


class Rook(Piece):
    def __init__(self, name, color):
        super().__init__(name, color)
        
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        return (start_row == end_row and start_col != end_col) or (start_col == end_col and start_row != end_row)