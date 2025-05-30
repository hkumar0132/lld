import uuid
from collections import defaultdict
from .PlayingPiece import PlayingPiece

class Board:
    def __init__(self) -> None:
        self.board_id = uuid.uuid4()
        self.position = defaultdict()

    def update_board(self, row, col, playing_piece: PlayingPiece):
        self.position[(row,col)] = playing_piece