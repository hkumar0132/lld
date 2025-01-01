from abc import ABC, abstractmethod

class IInternalButtonDispatcher(ABC):

    @abstractmethod
    def dispatch():
        pass