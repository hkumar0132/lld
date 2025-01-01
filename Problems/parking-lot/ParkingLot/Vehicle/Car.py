from VehicleType import VehicleType
from IVehicle import IVehicle

class Car(IVehicle):
    def __init__(self, vehicle_no) -> None:
        super().__init__(vehicle_no, VehicleType.FOUR_WHEELER)
