from Strategy import NormalDrive

from .Vehicle import Vehicle

class NormalVehicle(Vehicle):
    def __init__(self) -> None:
        super().__init__(NormalDrive())