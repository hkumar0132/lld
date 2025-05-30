from enums.PieceColor import PieceColor
from enums.PieceType import PieceType

import uuid

class Piece:
    def __init__(self, piece_name: PieceType, piece_color: PieceColor) -> None:
        self.piece_id = uuid.uuid4()
        self.piece_name = piece_name
        self.piece_color = piece_color