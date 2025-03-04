from exceptions.DuplicateException import DuplicateException
from exceptions.NotFoundException import NotFoundException
from models.ParkingFloor import ParkingFloor
from models.ParkingTicket import ParkingTicket
from enums.ParkingStrategies import ParkingStrategies
from enums.ParkingSpotStatus import ParkingSpotStatus
from .TicketService import TicketService
from .GateService import GateService

from threading import Lock

class ParkingLotService:
    def __init__(self, ticket_service: TicketService, gate_service: GateService) -> None:
        self.parking_floors = []
        self.ticket_service = ticket_service
        self.gate_service = gate_service
        self.lock = Lock()

    def get_available_parking_spots(self):
        pass

    def park_vehicle(self, vehicle, entry_gate_id, strategy: ParkingStrategies):

        if strategy == ParkingStrategies.FIRST_AVAILABLE:
            for floor in self.parking_floors:
                spot_id = floor.park_vehicle(vehicle)
                
                if spot_id:
                    parking_ticket = self.gate_service.enter_vehicle(entry_gate_id, spot_id, vehicle.id)

                    print(f'Vehicle parked on floor {floor.id} on spot with {spot_id}')
                    return parking_ticket
    
        raise NotFoundException("No parking spot available")

    def unpark_vehicle(self, parking_ticket, vehicle, exit_gate_id):
        for floor in self.parking_floors:
            spot_id = floor.unpark_vehicle(parking_ticket.parking_spot_id, vehicle)
            if spot_id:
                print(f'Vehicle unparked from {floor.id} and spot {parking_ticket.parking_spot_id}')
                self.gate_service.exit_vehicle(exit_gate_id, spot_id)
        
        raise NotFoundException("Vehicle not parked at this spot")

    def get_available_parking_spots_by_vehicle_type(vehicle_type):
        pass

    def add_floor(self, id, parking_spots):
        for floor in self.get_floor_by_id:
            if floor.id == id:
                raise DuplicateException(f"Floor with id {id} already exists")
        
        floor = ParkingFloor(id, parking_spots)
        self.parking_floors.append(floor)

    def get_floor_by_id(self):
        pass