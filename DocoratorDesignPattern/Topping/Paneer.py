from Topping.Topping import Topping

class Paneer(Topping):
    def __init__(self, pizza):
        self.pizza_cost = pizza.cost()
    
    def cost(self):
        return 70 + self.pizza_cost