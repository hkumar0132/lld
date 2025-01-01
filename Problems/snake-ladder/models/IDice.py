from abc import ABC, abstractmethod

from .DiceType import DiceType

class IDice(ABC):

    def __init__(self, type: DiceType) -> None:
        self.type = type

    @abstractmethod
    def roll_dice(self):
        pass