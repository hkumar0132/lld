from Topping.Paneer import Paneer
from Topping.Mushroom import Mushroom
from Topping.ExtraCheese import ExtraCheese
from Pizza.VegDelightPizza import VegDelightPizza
from Pizza.MargheritaPizza import MargheritaPizza
from Pizza.Pizza import Pizza
from Pizza.BasePizza import BasePizza


def main():
    pizza = Paneer(BasePizza())
    print(pizza.cost())

if __name__ == "__main__":
    main()