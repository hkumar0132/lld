from abc import ABC, abstractclassmethod

class Publisher(ABC):
    @abstractclassmethod
    def publish(self):
        pass