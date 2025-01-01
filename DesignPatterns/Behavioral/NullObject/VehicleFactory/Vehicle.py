from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def get_tank_capacity(self):
        pass

    @abstractmethod
    def get_seating_capacity(self):
        pass
    