from .Topping import Topping
from Pizza import BasePizza

class ExtraCheese(Topping):
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza
    
    def cost(self):
        return 50 + self.pizza.cost()