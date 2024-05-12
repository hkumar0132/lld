from abc import abstractmethod
from Pizza import BasePizza

class Topping(BasePizza):
    
    @abstractmethod
    def cost(self):
        pass