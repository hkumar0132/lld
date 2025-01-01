from typing import List

from models import BoardEntityType
from Snake import Snake
from Ladder import Ladder

class BoardEntityFactory:
    def get_entity(self, entity_type: BoardEntityType, head: List[int], tail: List[int]):
        if entity_type == BoardEntityType.LADDER:
            return Ladder(head, tail)
        elif entity_type == BoardEntityType.SNAKE:
            return Snake(head, tail)