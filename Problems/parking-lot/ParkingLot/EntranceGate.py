from Ticket import Ticket
from Vehicle import IVehicle

class EntranceGate:
    def __init__(self, parking_spot_manager_factory) -> None:
        self.parking_spot_manager_factory = parking_spot_manager_factory

    def park_vehicle(self):
        pass

    def find_space(self):
        pass

    def generate_ticket(self, vehicle: IVehicle):
        return Ticket(vehicle, "current time")