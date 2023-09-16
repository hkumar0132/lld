from Pizza.Pizza import Pizza

class VegDelightPizza(Pizza):
    def __init__(self, pizza):
        self.pizza_cost = pizza.cost()
        
    def cost(self):
        return 300 + self.pizza_cost