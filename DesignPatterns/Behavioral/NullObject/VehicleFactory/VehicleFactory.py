from .Bike import Bike
from .Car import Car
from .NullVehicle import NullVehicle
from .Vehicle import Vehicle

class VehicleFactory:

    def get_vehicle(self, vehicle_type) -> Vehicle:

        if vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "car":
            return Car()
        return NullVehicle()