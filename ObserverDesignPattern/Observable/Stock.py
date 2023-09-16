from abc import ABC, abstractclassmethod

class Stock(ABC):
    @abstractclassmethod
    def add(self):
        pass
    
    @abstractclassmethod
    def remove(self):
        pass
    
    @abstractclassmethod
    def get_stock_count(self):
        pass
    
    @abstractclassmethod
    def set_stock_count(self):
        pass
        
    @abstractclassmethod
    def notify(self):
        pass