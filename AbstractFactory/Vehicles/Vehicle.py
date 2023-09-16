from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def drive():
        pass