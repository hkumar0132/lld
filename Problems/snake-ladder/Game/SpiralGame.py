from GameStrategy import IGameStrategy, SpiralTraversal

class SpiralGame(IGameStrategy):
    def __init__(self) -> None:
        super().__init__(SpiralTraversal())