from Topping import Paneer, Mushroom, ExtraCheese
from Pizza import VegDelightPizza, MargheritaPizza, BasePizza

def main():
    pizza = ExtraCheese(ExtraCheese(Paneer(MargheritaPizza())))
    print(pizza.cost())

if __name__ == "__main__":
    main()