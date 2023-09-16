
from Strategy.SpecialDriveStrategy import SpecialDriveStrategy
from Vehicle.Vehicle import Vehicle

class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())
