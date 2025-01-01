from models import IPiece, PieceType

class PieceX(IPiece):
    def __init__(self) -> None:
        super().__init__(PieceType.X)

    def get_piece_type(self):
        return self.piece_type