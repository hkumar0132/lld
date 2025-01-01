from Strategy import SpecialDrive

from .Vehicle import Vehicle

class SpecialVehicle(Vehicle):
    def __init__(self) -> None:
        super().__init__(SpecialDrive())