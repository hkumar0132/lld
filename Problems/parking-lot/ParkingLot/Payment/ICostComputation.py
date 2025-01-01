from abc import ABC, abstractmethod

class ICostComputation(ABC):
    
    @abstractmethod
    def calculate_charges():
        pass