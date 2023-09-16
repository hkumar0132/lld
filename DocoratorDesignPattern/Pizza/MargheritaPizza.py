from Pizza.Pizza import Pizza

class MargheritaPizza(Pizza):
    def __init__(self, pizza):
        self.pizza_cost = pizza.cost()
        
    def cost(self):
        return 200 + self.pizza_cost