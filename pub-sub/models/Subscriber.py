from abc import ABC, abstractclassmethod

class Subscriber(ABC):
    
    @abstractclassmethod
    def get_id(self):
        pass
    
    @abstractclassmethod
    def update(self):
        pass