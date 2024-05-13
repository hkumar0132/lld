from models.Vehicle import Vehicle
from models.VehicleType import VehicleType


class Bike(Vehicle):
    def __init__(self, registration_no, color):
        super().__init__(VehicleType.BIKE, registration_no, color)