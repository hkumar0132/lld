from .Stock import Stock
from Observer import Alert

from typing import List

class IphoneStock(Stock):
    
    def __init__(self):
        self.observers: List[Alert] = []
        self.stock_count = 0
    
    def add(self, observer):
        self.observers.append(observer)
    
    def remove(self, observer):
        self.observers.remove(observer)
        
    def get_stock_count(self):
        return self.stock_count
    
    def set_stock_count(self, new_stocks):
        if self.stock_count == 0 and new_stocks != 0:
            self.stock_count += new_stocks
            self.notify()
    
    def notify(self):
        for observer in self.observers:
            observer.update()
            