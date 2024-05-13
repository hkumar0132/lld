from models.PlayingPiece import PlayingPiece
from models.PieceType import PieceType


class PlayingPieceEmpty(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.PieceTypeEmpty)