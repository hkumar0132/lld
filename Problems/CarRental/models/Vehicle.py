from models.Enums.VehicleStatus import VehicleStatus
from models.Enums.VehicleTypes import VehicleTypes

class Vehicle:
    def __init__(self, type: VehicleTypes, reg_no, status=VehicleStatus.AVAILABLE) -> None:
        self.type = type
        self.reg_no = reg_no
        self.status = status

    def change_vehicle_status(self, status: VehicleStatus):
        self.status = status