from enums.PieceColor import PieceColor
from enums.PieceType import PieceType
from .Piece import Piece

class Queen(Piece):
    def __init__(self, piece_id, piece_name, piece_color) -> None:
        super().__init__(piece_id, piece_name, piece_color)