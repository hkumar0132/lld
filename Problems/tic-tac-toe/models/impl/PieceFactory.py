from models import PieceType

from .PieceO import PieceO
from .PieceX import PieceX
from .PieceEmpty import PieceEmpty

class PieceFactory:

    def get_piece(self, piece_type):
        if piece_type == PieceType.O:
            return PieceO()
        elif piece_type == PieceType.X:
            return PieceX()
        return PieceEmpty()
