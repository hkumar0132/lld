import uuid
from enums.PlayingPieceType import PlayingPieceType

class Player:
    def __init__(self, name, email, mobile_no, country, playing_piece_type: PlayingPieceType) -> None:
        self.player_id = uuid.uuid4()
        self.name = name
        self.email = email
        self.mobile_no = mobile_no
        self.country = country
        self.playing_piece_type = playing_piece_type

    def update_name(self, name):
        self.name = name

    def update_playing_piece_type(self, playing_piece_type: PlayingPieceType):
        self.playing_piece_type = playing_piece_type