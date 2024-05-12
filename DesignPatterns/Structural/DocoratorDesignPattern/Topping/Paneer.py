from .Topping import Topping
from Pizza import BasePizza

class Paneer(Topping):
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza
    
    def cost(self):
        return 100 + self.pizza.cost()