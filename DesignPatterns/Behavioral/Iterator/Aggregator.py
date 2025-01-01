from abc import ABC, abstractmethod

class Aggregator(ABC):
    @abstractmethod
    def create_iterator(self):
        pass