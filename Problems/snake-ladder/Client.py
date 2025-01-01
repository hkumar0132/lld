from typing import List

from models import IBoardEntity, BoardEntityType
from Player import Player
from Game import Game
from BoardEntityFactory import BoardEntityFactory
from OneToSixDice import OneToSixDice

'''
Simpler solution in interviews will be using left to right traversal
in every row from top to bottom
and using normal positions (1, 2, ...) and translating it to [row, col]

[0, 1, 2, 3, 4, 5, ....10],
[11, 12, 13, 14, 15, ....20],
[],
.
.
.
[91, 92, ...., 100]

# @TODO -> get cell based on position (0, 1, 2, 3, ...) => [(0, 0), (0, 1), ...etc.]
def get_cell_position(self, position):
    return [
            position // self.N,
            position % self.N
        ]
'''

class Client:
    N = 20

    board_entity_factory = BoardEntityFactory()
    snake1 = board_entity_factory.get_entity(BoardEntityType.SNAKE, [9, 5], [3, 5])
    snake2 = board_entity_factory.get_entity(BoardEntityType.SNAKE, [0, 6], [4, 1])
    snake3 = board_entity_factory.get_entity(BoardEntityType.SNAKE, [0, 4], [2, 8])
    ladder1 = board_entity_factory.get_entity(BoardEntityType.LADDER, [2, 5], [1, 5])
    ladder2 = board_entity_factory.get_entity(BoardEntityType.LADDER, [9, 6], [7, 9])
    ladder3 = board_entity_factory.get_entity(BoardEntityType.LADDER, [1, 2], [0, 1])

    entities: List[IBoardEntity] = [
        snake1, snake2, snake3, ladder1, ladder2, ladder3
    ]

    dice = OneToSixDice()
    
    game = Game(N, entities, [dice])

    player1 = Player(1, "A")
    player2 = Player(2, "B")
    player3 = Player(3, "C")
    
    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)

    game.start_game()