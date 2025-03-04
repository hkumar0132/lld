from enums.GameState import GameState

class Game:
    def __init__(self, player_a_id, player_b_id, player_a_piece_type, player_b_piece_type, timer_a_id, timer_b_id, game_state: GameState.ONGOING) -> None:
        self.player_a_id = player_a_id
        self.player_b_id = player_b_id
        self.player_a_piece_type = player_a_piece_type
        self.player_b_piece_type = player_b_piece_type
        self.timer_a_id = timer_a_id
        self.timer_b_id = timer_b_id
        self.turn = None
        self.game_state = game_state
        self.history = []