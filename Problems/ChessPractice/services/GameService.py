from models.Game import Game
from .PieceService import PieceService
from .PlayerService import PlayerService

class GameService:

    def __init__(self, piece_service: PieceService, player_service: PlayerService) -> None:
        # initialization of game 
        # piece creation and setup on board
        self.game = Game()

    def start_game(self):
        pass

    def check_if_won(self):
        pass

    def check_if_draw(self):
        pass