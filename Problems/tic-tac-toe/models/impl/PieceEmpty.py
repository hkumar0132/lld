from models import IPiece, PieceType

class PieceEmpty(IPiece):
    def __init__(self) -> None:
        super().__init__(PieceType.EMPTY)

    def get_piece_type(self):
        return self.piece_type