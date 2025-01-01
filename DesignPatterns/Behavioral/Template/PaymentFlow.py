from abc import ABC, abstractmethod

class PaymentFlow(ABC):

    @abstractmethod
    def validate_request(self):
        pass

    @abstractmethod
    def debit_money(self):
        pass

    # Common method
    def calculate_fees(self):
        pass

    # Common method
    def credit_money(self):
        pass

    def send_money(self):
        self.validate_request()
        self.debit_money()
        self.calculate_fees()
        self.credit_money()