from typing import List

from models import IBoardEntity, BoardEntityType

class Ladder(IBoardEntity):
    def __init__(self, head, tail) -> None:
        super().__init__(head, tail, BoardEntityType.LADDER)

    def get_type(self):
        return self.type
        
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail