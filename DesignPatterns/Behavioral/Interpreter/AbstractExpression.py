from abc import ABC, abstractmethod

from Context import Context

class AbstractExpression(ABC):

    @abstractmethod
    def interpret(self, context: Context):
        pass