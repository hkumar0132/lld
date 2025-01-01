from models import IPlayer, PieceType

class Player(IPlayer):

    def __init__(self, name: str, id: int, piece_type: PieceType) -> None:
        self.name = name
        self.id = id
        self.piece_type = piece_type

    def get_player_name(self):
        return self.name

    def get_player_id(self):
        return self.id
    
    def get_piece_type(self):
        return self.piece_type