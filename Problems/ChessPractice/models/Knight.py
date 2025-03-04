from enums.PieceColor import PieceColor
from enums.PieceType import PieceType
from .Piece import Piece

class Knight(Piece):
    def __init__(self, piece_name, piece_color) -> None:
        super().__init__(piece_name, piece_color)