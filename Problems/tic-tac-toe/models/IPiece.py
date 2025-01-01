from abc import ABC, abstractmethod

class IPiece(ABC):
    def __init__(self, piece_type) -> None:
        self.piece_type = piece_type
        
    @abstractmethod
    def get_piece_type(self):
        pass