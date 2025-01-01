from VehicleType import VehicleType
from IVehicle import IVehicle

class Bike(IVehicle):
    def __init__(self, vehicle_no) -> None:
        super().__init__(vehicle_no, VehicleType.TWO_WHEELER)
