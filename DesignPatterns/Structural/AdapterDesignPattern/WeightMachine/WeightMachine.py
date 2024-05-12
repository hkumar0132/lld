from abc import ABC, abstractmethod

class WeightMachine(ABC):

    @abstractmethod
    def get_weight_in_pounds():
        pass