from models.Vehicle import Vehicle
from models.VehicleType import VehicleType


class Truck(Vehicle):
    def __init__(self, registration_no, color):
        super().__init__(VehicleType.TRUCK, registration_no, color)
        
    