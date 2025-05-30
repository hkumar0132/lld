from enums.PlayingPieceType import PlayingPieceType

from models.PlayingPieceEmpty import PlayingPieceEmpty
from models.PlayingPieceX import PlayingPieceX
from models.PlayingPieceY import PlayingPieceY

class PieceFactory:

    @staticmethod
    def get_playing_piece_by_type(piece_type: PlayingPieceType):

        if piece_type == PlayingPieceType.EMPTY:
            return PlayingPieceEmpty()
        elif piece_type == PlayingPieceType.X:
            return PlayingPieceX()
        elif piece_type == PlayingPieceType.Y:
            return PlayingPieceY()