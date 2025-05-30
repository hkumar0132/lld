from models.Piece import Piece
from exceptions.InvalidMove import InvalidMove

class PieceService:
    def __init__(self) -> None:
        self.pieces = []

    def create_piece(self, piece_id, piece_type):
        pass

    def remove_piece(self, piece_id):
        pass

    def validate_move(self, piece: Piece):
        # -> If invalid move -> return InvalidMove("Move is not valid")
        pass
