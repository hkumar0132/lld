from abc import ABC, abstractmethod

class IExternalButtonDispatcher(ABC):

    @abstractmethod
    def dispatch():
        pass