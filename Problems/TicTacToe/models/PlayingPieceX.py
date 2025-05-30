import uuid

from enums.PlayingPieceType import PlayingPieceType
from models.PlayingPiece import PlayingPiece

class PlayingPieceX(PlayingPiece):
    def __init__(self) -> None:
        super().__init__(PlayingPieceType.X)