from abc import abstractclassmethod
from Pizza.BasePizza import BasePizza

class Topping(BasePizza):
    
    @abstractclassmethod
    def cost(self):
        pass