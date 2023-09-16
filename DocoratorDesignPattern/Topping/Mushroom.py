from Topping.Topping import Topping

class Mushroom(Topping):
    def __init__(self, pizza):
        self.pizza_cost = pizza.cost()
    
    def cost(self):
        return 200 + self.pizza_cost