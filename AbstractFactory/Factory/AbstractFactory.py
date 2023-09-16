from abc import ABC, abstractclassmethod

class AbstractFactory(ABC):
    @abstractclassmethod
    def get_vehicle():
        pass