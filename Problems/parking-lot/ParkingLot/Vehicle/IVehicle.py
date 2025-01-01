from VehicleType import VehicleType

class IVehicle:
    def __init__(self, vehicle_no, vehicle_type: VehicleType) -> None:
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type