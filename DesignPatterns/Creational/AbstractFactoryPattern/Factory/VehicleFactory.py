from .Abstract.LuxuryVehicleFactory import LuxuryVehicleFactory
from .Abstract.OrdinaryVehicleFactory import OrdinaryVehicleFactory

class VehicleFactory:

    def get_vehicle_factory(self, vehicle_type):
        if vehicle_type == "LUXURY":
            return LuxuryVehicleFactory()
        elif vehicle_type == "ORDINARY":
            return OrdinaryVehicleFactory()