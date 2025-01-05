from models.User import User
from models.Driver import Driver
from models.Vehicle.Vehicle import Vehicle
from models.Location import Location
from models.Vehicle.VehicleFactory import VehicleFactory
from exceptions.DuplicateUsername import DuplicateUsernameException
from exceptions.NotFound import NotFoundException
from models.Enums.VehicleTypes import VehicleTypes

class DriverService:
    def __init__(self) -> None:
        self.drivers: list[Driver] = []

    def add_driver(self, username, name, age, gender, vehicle_type: VehicleTypes, vehicle_model_no, vehicle_reg_no, location: Location):
        for driver in self.drivers:
            if driver.username == username:
                raise DuplicateUsernameException('Driver already exists')
            
        vehicle_factory = VehicleFactory()
        vehicle = vehicle_factory.get_vehicle(vehicle_type, vehicle_model_no, vehicle_reg_no)
        user = User(
            username,
            name,
            age,
            gender,
            location
        )
        driver = Driver(
            user,
            vehicle,
        )

        self.drivers.append(driver)

        print("Driver added")
        return driver
    
    def update_driver_location(self, username, location: Location):
        for driver in self.drivers:
            if driver.username == username:
                driver.update_driver_location(location)
                print("Driver location updated")
                return
        
        raise NotFoundException('Driver not found')
        
    def change_driver_status(self, username, location: Location):
        for driver in self.drivers:
            if driver.username == username:
                driver.change_driver_status(location)
                print("Driver status updated")
                return
        
        raise NotFoundException('Driver not found')
    
    def get_all_drivers(self):
        return self.drivers
    
    def get_driver_by_username(self, username):
        for driver in self.drivers:
            if driver.username == username:
                return driver