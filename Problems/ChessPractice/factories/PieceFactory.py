from enums.PieceColor import PieceColor
from enums.PieceType import PieceType
from models.Knight import Knight
from models.King import King
from models.Queen import Queen
from models.Pawn import Pawn
from models.Rook import Rook
from models.Bishop import Bishop

class PieceFactory:
    @staticmethod
    def get_piece(piece_type: PieceType, piece_color: PieceColor):
        if piece_type == PieceType.KNIGHT:
            return Knight(piece_type, piece_color)
        elif piece_type == PieceType.KING:
            return King(piece_type, piece_color)
        elif piece_type == PieceType.QUEEN:
            return Queen(piece_type, piece_color)
        elif piece_type == PieceType.PAWN:
            return Pawn(piece_type, piece_color)
        elif piece_type == PieceType.ROOK:
            return Rook(piece_type, piece_color)
        elif piece_type == PieceType.BISHOP:
            return Bishop(piece_type, piece_color)