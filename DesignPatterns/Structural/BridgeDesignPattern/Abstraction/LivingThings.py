from abc import ABC, abstractmethod
from Implementor import BreatheImplementor

class LivingThings(ABC):

    def __init__(self, implementor: BreatheImplementor) -> None:
        self.implementor = implementor

    @abstractmethod
    def breathe_process(self):
        pass