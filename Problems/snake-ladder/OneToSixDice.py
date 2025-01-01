from random import randint

from models import DiceType, IDice

class OneToSixDice(IDice):

    def __init__(self) -> None:
        super().__init__(DiceType.ONE_TWO_SIX)

    def roll_dice(self):
        return randint(1, 6)