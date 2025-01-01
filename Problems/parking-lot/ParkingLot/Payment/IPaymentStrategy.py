from abc import ABC, abstractmethod

class IPaymentStrategy(ABC):
    
    @abstractmethod
    def calculate_parking_charge(self):
        pass