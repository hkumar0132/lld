from Topping.Topping import Topping

class ExtraCheese(Topping):
    def __init__(self, pizza):
        self.pizza_cost = pizza.cost()
    
    def cost(self):
        return 50 + self.pizza_cost