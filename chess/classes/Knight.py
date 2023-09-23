from model.Piece import Piece


class Knight(Piece):
    def __init__(self, name, color):
        super().__init__(name, color)
        
    '''
    (0,0) (0,1) (0,2)
    (1,0) (1,1) (1,2)
    (2,0) (2,1) (2,2)
    
    '''
        
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        return ((end_row == start_row + 2 or end_row == start_row - 2) and (end_col == start_col + 1 or end_col == start_col - 1)) or ((end_col == start_col + 2 or end_col == start_col - 2) and (end_row == start_row + 1 or end_row == start_row - 1))