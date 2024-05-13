from models.Vehicle import Vehicle
from models.VehicleType import VehicleType


class Car(Vehicle):
    def __init__(self, registratio_no, color):
        super().__init__(VehicleType.CAR, registratio_no, color)
        
    