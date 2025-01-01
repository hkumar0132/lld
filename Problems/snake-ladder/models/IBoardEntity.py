from abc import ABC, abstractmethod

from .BoardEntityType import BoardEntityType

class IBoardEntity(ABC):
    def __init__(self, head, tail, type: BoardEntityType) -> None:
        self.head = head
        self.tail = tail
        self.type = type

    @abstractmethod
    def get_type(self):
        return self.type
        
    @abstractmethod
    def get_head(self):
        pass
    
    @abstractmethod
    def get_tail(self):
        pass