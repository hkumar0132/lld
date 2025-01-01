from abc import ABC, abstractmethod

class IExpression(ABC):

    @abstractmethod
    def evaluate(self):
        pass