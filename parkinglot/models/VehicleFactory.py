from classes.Bike import Bike
from classes.Car import Car
from classes.Truck import Truck
from models.VehicleType import VehicleType


class VehicleFactory:
    def get_vehicle(self, vehicle_type, *args):
        print('VehicleFactory: ', args)
        if vehicle_type == VehicleType.TRUCK:
            return Truck(*args)
        elif vehicle_type == VehicleType.CAR:
            return Car(*args)
        elif vehicle_type == VehicleType.BIKE:
            return Bike(*args)
        
        print('\nInvalid vehicle type')
        return None