from Vehicle import IVehicle
from Payment import IPaymentStrategy

class Ticket:
    def __init__(self, vehicle: IVehicle, entry_time: str, payment_strategy: IPaymentStrategy) -> None:
        pass

    def generate_ticket_id(self):
        return "TICKET ID"