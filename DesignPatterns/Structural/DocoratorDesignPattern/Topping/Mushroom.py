from .Topping import Topping
from Pizza import BasePizza

class Mushroom(Topping):
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza
    
    def cost(self):
        return 75 + self.pizza.cost()