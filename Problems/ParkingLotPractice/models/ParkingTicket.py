class ParkingTicket:
    def __init__(self, id, entry_time, exit_time, parking_spot_id, vehicle_id) -> None:
        self.id = id
        self.parking_spot_id = parking_spot_id
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.vehicle_id = vehicle_id

    def generate_ticket(self):
        pass