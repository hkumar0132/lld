
from Strategy.NormalDriveStrategy import NormalDriveStrategy
from Vehicle.Vehicle import Vehicle

class NormalVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())