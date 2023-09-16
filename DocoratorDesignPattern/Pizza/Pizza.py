from abc import ABC, abstractclassmethod

class Pizza(ABC):
    
    @abstractclassmethod
    def cost(self):
        pass