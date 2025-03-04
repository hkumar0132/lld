from enums.ParkingSpotStatus import ParkingSpotStatus
from enums.VehicleType import VehicleType
from exceptions.NotFoundException import NotFoundException
from threading import Lock

class ParkingSpot:
    def __init__(self, id, vehicle_type: VehicleType, status=ParkingSpotStatus.AVAILABLE) -> None:
        self.id = id
        self.status = status
        self.vehicle_type = vehicle_type
        self.vehicle = None

        self.lock = Lock()
    
    def park_vehicle(self, vehicle):
        with self.lock:
            if self.status == ParkingSpotStatus.AVAILABLE and vehicle.type == self.vehicle_type:
                self.vehicle = vehicle
                self.status = ParkingSpotStatus.OCCUPIED
                return True
            return False
    
    def unpark_vehicle(self, vehicle):
        if vehicle.id != self.vehicle.id:
            return

        self.vehicle = None
        return self.id
    
    def get_vehicle(self):
        return self.vehicle

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status