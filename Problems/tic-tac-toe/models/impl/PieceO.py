from models import IPiece, PieceType

class PieceO(IPiece):
    def __init__(self) -> None:
        super().__init__(PieceType.O)

    def get_piece_type(self):
        return self.piece_type