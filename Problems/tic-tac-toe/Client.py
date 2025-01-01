from Game import Game
from models.impl import Player
from models import PieceType

class Client:
    game = Game()

    player1 = Player("A", 1, PieceType.X)
    player2 = Player("B", 2, PieceType.O)
    game.initialize_game(3, [
        player1,
        player2
    ])

    game.start_game()