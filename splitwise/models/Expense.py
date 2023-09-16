from abc import ABC, abstractclassmethod

class Expense(ABC):
    @abstractclassmethod
    def get_paid_by(self):
        pass
    
    @abstractclassmethod
    def get_amount(self):
        pass
    
    @abstractclassmethod
    def get_split_into(self):
        pass