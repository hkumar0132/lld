from .PlayerManagementService import PlayerManagementService
from models.Game import Game
from typing import List

class GameService:
    def __init__(self, player_service: PlayerManagementService) -> None:
        self.player_service = player_service
        self.game = None
        
    def start_game(self):
        self.game = Game()
        pass

    def pause_game(self):
        pass

    def check_if_won(self):
        pass

    def check_if_draw(self):
        pass

    def validate_move(self, starting_position: List[int], ending_position: List[int]):
        # If invalid move -> InvalidMoveException(f"cannot move from {starting_position} to {ending_position}")
        pass