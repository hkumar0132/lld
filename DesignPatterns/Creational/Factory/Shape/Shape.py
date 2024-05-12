from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def draw(self):
        pass