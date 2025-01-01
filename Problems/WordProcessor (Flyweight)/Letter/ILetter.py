from abc import ABC, abstractmethod

class ILetter(ABC):

    @abstractmethod
    def display(row: int, col: int):
        pass