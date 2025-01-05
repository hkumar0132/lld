from models.Enums.VehicleTypes import VehicleTypes
from .Car import Car
from .Auto import Auto
from exceptions.NotFound import NotFoundException

class VehicleFactory:
    def get_vehicle(self, vehicle_type: VehicleTypes, vehicle_model_no: str, vehicle_reg_no: str):
        if vehicle_type == VehicleTypes.AUTO:
            return Auto(vehicle_model_no, vehicle_reg_no)
        elif vehicle_type == VehicleTypes.CAR:
            return Car(vehicle_model_no, vehicle_reg_no)

        raise NotFoundException('Vehicle Type not fund')