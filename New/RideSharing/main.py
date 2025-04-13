'''
Design Ride sharing 

Actors:
Driver
Riders

Requirements:
    
1. Ride booking
    - First available driver
    - Extensible to other strategies
2. Searching for available drivers 
    - location
3. Fare calculation
    - Simple distance based calculation
    
Core Entities:
    
1. Rider
2. Driver
3. Ride
4. Location - lat, long, pincode
5. RideMatching
    - FirstAvailableRideMatching
        - give_available_drivers()
    - Strategy design pattern 
6. FareCalculator
    - DistanceBasedFareCalculation
    - FirsAvailableFareCalculation

'''

# Classes Design:
    
enums/
from enum import Enum
class DriverStatus(Enum):
    AVAILABLE='AVAILABLE'
    DRIVING='DRIVING'
    INACTIVE='INACTIVE'

class RideStatus(Enum):
    PENDING='PENDING'
    CONFIRMED='CONFIRMED'
    STARTED='STARTED'
    COMPLETED='COMPLETED'
    CANCELLED='CANCELLED'

models/
class Location:
    def __init__(self, lat: str, long: str, pincode: str, city: str, country: str):
        self.lat = lat
        self.long = long
        self.pincode = pincode
        self.city = city

class Vehicle:
    def __init__(self, model: str, reg_no: str, slots: int):
        self.model = model
        self.reg_no = reg_no
        self.max_slots = slots
        self.current_slot = slots

    def get_slots(self):
        return self.slots
    
    def update_slots(self, slot_count: int, type='decrement'):
        if type == 'decrement':
            self.current_slot -= slot_count
        else:
            self.current_slot += slot_count
    
    def reset_current_slot(self):
        self.current_slot = self.max_slots

class User:
    def __init__(self, name: str, email: str, location: Location=None) -> None:
        self.name = name
        self.email = email
        self.location = location

    def update_location(self, new_location: Location):
        self.location = new_location


class Rider(User):
    def __init__(self, name: str, email: str, location: Location=None):
        super().__init__(name, email, location)
            
class Driver(User):
    
    def __init__(self, name: str, email: str, vehicle: Vehicle, status: DriverStatus, location: Location, slots: int):
        super().__init__(name, email)
        self.vehicles = vehicle
        self.status = status
        self.location = location
        self.slots = slots
        
    def get_status(self):
        return self.status
        
    def update_status(self, new_status: DriverStatus):
        self.status = new_status

        
class Ride:
    
    def __init__(self, source: Location, destination: Location, rider: Rider, fare: int, status: RideStatus=RideStatus.PENDING, driver: Driver=None):
        self.source = source
        self.destination = destination
        self.rider = rider
        self.fare = fare
        self.status = status
        self.driver = driver

    def update_driver(self, driver: Driver):
        self.driver = driver

    def update_status(self, new_status: RideStatus):
        if self.status == RideStatus.COMPLETED and new_status == RideStatus.STARTED:
            raise Exception('Invalid status update')
        self.status = new_status

from abc import ABC, abstractmethod
class FareCalculator:
    @abstractmethod
    def calculate_fare(self):
        pass

import math
class DistanceBasedFareCalculator(FareCalculator):
    def calculate_fare(self, source: Location, destination: Location):
        return DISTANCE_MULTIPLIER * math.sqrt(destination.lat * destination.lat - source.lat * source.lat + destination.long * destination.long - source.long * source.long)
    

from abc import ABC, abstractmethod
class RideMatching(ABC):
    @abstractmethod
    def get_available_driver(self):
        pass
    
from typing import List    
class FirstAvailableRideMatching(RideMatching):
    def __init__(self, drivers: List[Driver]):
        self.drivers = drivers
    
    def get_available_driver(self):
        for driver in self.drivers:
            if driver.get_status() == DriverStatus.AVAILABLE and driver.vehicle.get_slots() > 0:
                return driver                        

constants/
DISTANCE_MULTIPLIER = 10
    
services/

class FareService:

    def __init__(self, calculation_strategy: FareCalculator) -> None:
        self.calculation_strategy = calculation_strategy
    
    def calculate_fare(self, source: Location, destination: Location):
        return self.calculation_strategy.calculate_fare(source, destination)

from threading import Lock
class RideService:
    
    def __init__(self, fare_service: FareService, searching_strategy: RideMatching):
        self.fare_service = fare_service
        self.searching_strategy = searching_strategy
        self.rides = []
        self.driver_to_ride = dict()
        self.lock = Lock()
    
    def __search_available_driver(self, source: Location) -> Driver:
        driver = self.searching_strategy.get_available_driver(source)        
        return driver
    
    def __assign_driver_to_a_ride(self, ride: Ride):
        with self.lock:
            driver = self.__search_available_driver(ride.source)

            if not driver:
                raise NoAvailableDriverError()
                        
            driver.update_status(DriverStatus.DRIVING)
            ride.update_driver(driver)
        
    def create_a_ride(self, source: Location, destination: Location, rider: Rider) -> Ride:
        
        fare = self.fare_service.calculate_fare(source, destination)

        '''
            Maintain slots on vehicle

            if 5 slots -> 4 -> 3 -> 2 -> 1 -> 0
            0: RideStatus.CONFIRMED
            Maintain driver_to_ride
            If another rider matches with the same driver -> decrease the slot count

            driver.vehicle.update_slots(1, 'decrement')
        '''
        ride = Ride(
            source,
            destination,
            rider,
            fare,
            RideStatus.CONFIRMED
        )

        self.rides.append(ride)
        self.__assign_driver_to_a_ride(ride)
                        
        return ride
        

    def update_ride_status(self, ride: Ride, new_status: RideStatus):
        ride.update_status(new_status)
            
    def ride_end(self, ride: Ride):
        ride.driver.update_status(DriverStatus.AVAILABLE)
        ride.update_status(RideStatus.COMPLETED)

exceptions/        
class NoAvailableDriverError(Exception):
    def __init__(self, message="Driver not available") -> None:
        super().__init__(message)
        
controller/
def main():
    
    try:
        ride_service = RideService(....)
        
        ride = ride_service.create_a_ride(source, ..., )
        print(f"Ride confirmed with driver: {ride.driver.get_name()}")
         
        ride_service.ride_end()
    except NoAvailableDriverError as e:
        print(f"Unable to find a driver: {e}")
        return { "error": "Unable to find a driver" }

main()

'''
Pros:
- Ride matching strategy
- Clarified DB design or classes
- DriverStatus as enum is good
- MVC architecture good
- Dependency injection
- Exception handling handled by follow up

Cons/Suggestions:
- Fare Calculation inheritance
- Move fast, especially with Requirements (Not at the cost of quality)
- Ask for minimum requirements
- User class inheritance with Driver and Rider
- Security is a big deal: Never store password
- RideStatus is missing
- Change the ride status back to available: ride_end()
- Double booking: Don't go into details yourself
- Locking wasn't right
- Vehicle
- Ride Pool:
    - Slots count

'''
