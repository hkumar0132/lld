from .Location import Location
from .Vehicle.Vehicle import Vehicle
from .User import User
from .Enums.DriverStatus import DriverStatus

class Driver(User):
    def __init__(self, driver_details: User, vehicle_details: Vehicle) -> None:
        super().__init__(driver_details.username, driver_details.name, driver_details.age, driver_details.gender, driver_details.location)
        self.status = DriverStatus.ACTIVE
        self.driver_details = driver_details
        self.vehicle_details = vehicle_details

    def update_driver_location(self, location: Location):
        super().update_location(location)

    def change_driver_status(self, status):
        self.status = status
