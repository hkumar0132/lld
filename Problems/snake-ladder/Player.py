from typing import List

from models import IPlayer

class Player(IPlayer):

    def __init__(self, player_id: int, player_name: str) -> None:
        self.player_id = player_id
        self.player_name = player_name

    def get_player_id(self):
        return self.player_id

    def get_player_name(self):
        return self.player_name

    def set_position(self, position: List[int]):
        self.position = position

    def get_position(self):
        return self.position