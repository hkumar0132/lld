import uuid

from enums.PlayingPieceType import PlayingPieceType

class PlayingPiece:
    def __init__(self, playing_piece_type: PlayingPieceType) -> None:
        self.playing_piece_id = uuid.uuid4()
        self.playing_piece_type = playing_piece_type