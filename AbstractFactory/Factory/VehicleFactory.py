from Factory.LuxuryVehicle import LuxuryVehicle
from Factory.OrdinaryVehicle import OrdinaryVehicle


class VehicleFactory:
    
    def get_vehicle_type(self, luxury):
        if luxury:
            return LuxuryVehicle()
        return OrdinaryVehicle()