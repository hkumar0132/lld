from collections import defaultdict

class Board:
    def __init__(self, board_id, position=defaultdict()) -> None:
        self.board_id = board_id
        self.position = position

    def update_board(self, row, col, piece):
        self.position[(row,col)] = piece