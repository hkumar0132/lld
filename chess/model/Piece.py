from abc import ABC, abstractclassmethod

class Piece(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    @abstractclassmethod
    def is_valid_move(self):
        pass