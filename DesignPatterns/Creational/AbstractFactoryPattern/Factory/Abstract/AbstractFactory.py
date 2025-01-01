from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def get_vehicle():
        pass