from abc import ABC, abstractmethod

class IRobot(ABC):

    @abstractmethod
    def display(x: int, y: int):
        pass