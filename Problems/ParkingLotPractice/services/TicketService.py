from models.ParkingTicket import ParkingTicket

class TicketService:
    def __init__(self) -> None:
        self.parking_tickets = []

    def generate_ticket(self, id, entry_time, exit_time, parking_spot_id, vehicle_id):
        parking_ticket = ParkingTicket(id, entry_time, exit_time, parking_spot_id, vehicle_id)
        return parking_ticket