from .AbstractFactory import AbstractFactory
from Vehicles import BMW, Mercedes

class LuxuryVehicleFactory(AbstractFactory):
    def get_vehicle(self, vehicle):
        if vehicle == "BMW":
            return BMW()
        elif vehicle == "Mercedes":
            return Mercedes()