from abc import ABC, abstractmethod

class Stock(ABC):
    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def get_stock_count(self):
        pass
    
    @abstractmethod
    def set_stock_count(self):
        pass
        
    @abstractmethod
    def notify(self):
        pass