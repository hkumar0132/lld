from enums.VehicleType import VehicleType
class Vehicle:
    def __init__(self, id, vehicle_no, user, vehicle_type: VehicleType) -> None:
        self.id = id
        self.vehicle_no = vehicle_no
        self.user = user
        self.vehicle_type = vehicle_type