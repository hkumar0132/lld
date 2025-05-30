import uuid

from enums.PlayingPieceType import PlayingPieceType
from models.PlayingPiece import PlayingPiece

class PlayingPieceEmpty(PlayingPiece):
    def __init__(self) -> None:
        super().__init__(PlayingPieceType.EMPTY)