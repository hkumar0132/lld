from abc import ABC, abstractmethod

class Adapter(ABC):

    @abstractmethod
    def get_weight_in_kg():
        pass