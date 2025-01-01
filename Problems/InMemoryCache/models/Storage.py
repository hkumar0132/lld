from abc import ABC, abstractclassmethod

class Storage(ABC):
    @abstractclassmethod
    def get(self):
        pass
    
    @abstractclassmethod
    def put(self):
        pass
    
    @abstractclassmethod
    def remove(self):
        pass
    