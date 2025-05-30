from enum import Enum

class GameState(Enum):
    ONGOING='ONGOING'
    CHECK='CHECK'
    CHECKMATE='CHECKMATE'
    DRAW='DRAW'
    STALEMATE='STALEMATE'