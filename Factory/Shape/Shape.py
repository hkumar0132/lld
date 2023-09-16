from abc import ABC, abstractclassmethod

class Shape(ABC):
    
    @abstractclassmethod
    def draw(self):
        pass