from .AbstractFactory import AbstractFactory
from Vehicles import Suzuki

class OrdinaryVehicleFactory(AbstractFactory):
    def get_vehicle(self, vehicle):
        if vehicle == "Suzuki":
            return Suzuki()