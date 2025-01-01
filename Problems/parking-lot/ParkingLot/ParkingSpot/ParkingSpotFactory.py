from Vehicle import VehicleType
from FourWheelerParkingSpotManager import FourWheelerParkingSpotManager
from TwoWheelerParkingSpotManager import TwoWheelerParkingSpotManager

class ParkingSpotFactory:

    def get_parking_spot_manager(vehicle_type: VehicleType):
        if vehicle_type == VehicleType.TWO_WHEELER:
            return TwoWheelerParkingSpotManager()
        elif vehicle_type == VehicleType.FOUR_WHEELER:
            return FourWheelerParkingSpotManager()