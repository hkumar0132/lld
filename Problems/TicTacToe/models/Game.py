import uuid

from enums.GameStatus import GameStatus

class Game:
    def __init__(self, board, player_ids, started_at, finished_at) -> None:
        self.game_id = uuid.uuid4()
        self.board = board
        self.player_ids = player_ids
        self.game_status = GameStatus.ONGOING
        self.started_at = started_at
        self.finished_at = finished_at

    def update_game_status(self, game_status: GameStatus):
        self.game_status = game_status