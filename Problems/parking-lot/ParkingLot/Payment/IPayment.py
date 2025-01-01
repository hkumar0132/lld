from abc import ABC, abstractmethod

class IPayment(ABC):

    @abstractmethod
    def make_payment(self):
        pass
    