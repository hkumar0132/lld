# Design Parking Lot
'''
Functional requirements:
    
1. Vehicle parking should be allowed
    a. One strategy but extendible - first available space
2. One Entry gate/Exit gate
3. Multiple floors
4. Multiple vehicles

Out of scope:
1. Pricing
2. Ticket
3. Vehicle management

Core Entities:
1. Vehicle
2. EntryGate
3. ExitGate
4. Floor
5. Spot
    - VipSpot
    - BasicSpot
6. ParkingStrategy
    - FirstAvailableParkingStrategy
7. VehicleType
   - Truck
   - Car
   - Bike
   
- Strategy design pattern

'''

# Python Implementation:
    
enums/
VehicleType.py

from enum import Enums
class VehicleType(Enum):
    TRUCK='TRUCK'
    CAR='CAR'
    BIKE='BIKE'
    
SpotStatus.py

class SpotStatus:
    UNDER_MAINTAINENCE='UNDER_MAINTAINENCE'
    AVAILABLE='AVAILABLE'
    OCCUPIED='OCCUPIED'
    
models/

import uuid
class Vehicle:
    def __init__(self, name: str, vehicle_reg_no: str, vehicle_type: VehicleType):
        self.name = name
        self.vehicle_reg_no = vehicle_reg_no
        self.vehicle_type = vehicle_type
    
class EntryGate:
    def __init__(self):
        pass
    
class ExitGate:
    def __init__(self):
        pass
    
class Spot:
    def __init__(self, vechile_type: VehicleType, status: SpotStatus='AVAILABLE')
        self.vehicle_type = vechile_type
        self.status = status
        self.vehicle = None
        
    def update_status(self, new_status: SpotStatus):
        self.status = new_status
        
    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.update_status(SpotStatus.OCCUPIED)
        
    def remove_vehicle(self, vehicle: Vehicle):
        if self.vehicle != vehicle:
            raise InvalidVehicleParking()
        self.vehicle = None
        self.update_status(SpotStatus.AVAILABLE)
    
import uuid
from typing import List
class Floor:
    def __init__(self, spots: List[Spot]):
        self.floor_id = uuid.uuid4()
        self.spots = spots
        
    def add_a_spot(self, spot: Spot):
        self.spots.append(spot)
    
    def remove_a_spot(self, spot_id: str):
        self.spots = [id != spot_id for id in self.spots]
        
    def get_available_spots(self, vehicle_type: VehicleType):
        for spot in self.spots:
            if spot.status == SpotStatus.AVAILABLE and spot.vehicle_type == vehicle_type:
                return spot
                
from abc import abstractmethod    
class ParkingStrategy:
    def __init__(self):
        pass
    
    @abstractmethod
    def get_parking_spot(self) -> Spot:
        pass
    
from Floor import Floor    
class FirstAvailableParkingStrategy(ParkingStrategy):
    
    def __init__(self, floors: List[Floor]):
        self.floors = floors
        
    def get_parking_spot(self, vehicle_type: VehicleType) -> Spot:
        for floor in self.floors:
            spot = floor.get_available_spots(vehicle_type)
            if spot:
                return spot
                
services/

VehicleService.py

class VehicleService:
    def __init__(self) -> None:
        self.vehicles = []

    def add_a_vehicle(self, vehicle_reg_no, vehicle_type: VehicleType):
        return Vehicle(vehicle_reg_no, vehicle_type)

FloorService.py

class FloorService:
    
    def __init__(self, number_of_floors: int, spots: int):
        self.floors = []
        
    def create_floor(self):
        for i in range(number_of_floors):
            spots = []
            for j in range(spots):
                spots.append(Spot(VehicleType.TRUCK))
            for j in range(spots):
                spots.append(Spot(VehicleType.CAR))                
            self.floors.append(Floor(spots))
    
    def get_floors(self):
        return self.floors
    
ParkingService.py
from threading import Lock
class ParkingService:
    
    def __init__(self, parking_strategy: FirstAvailableParkingStrategy):
        self.parking_strategy = parking_strategy
        self.lock = Lock()

    def __assign_parking_spot(self, vehicle: Vehicle):
        with self.lock:
            parking_spot = self.parking_strategy.get_parking_spot(vehicle.vehicle_type)
            if parking_spot:
                return None

            parking_spot.add_vehicle(vehicle)

            return parking_spot

    def park_vehicle(self, vehicle: Vehicle):
        parking_spot = self.__assign_parking_spot(vehicle)
        if not parking_spot:
            raise ParkingSpotUnavailable()
        return parking_spot

    def unpark_vehicle(self, vehicle: Vehicle, parking_spot: Spot):
        parking_spot.remove_vehicle(vehicle)

exceptions/
class ParkingSpotUnavailable(Exception):
    def __init__(self, message="Parking spot unavailable") -> None:
        super().__init__(message)

class InvalidVehicleParking(Exception):
    def __init__(self, message="Different vehicle parked here") -> None:
        super().__init__(message)

controller/

def main():

    try:
        floor_service = FloorService(5, 5)
        floor_service.create_floors()

        vehicle_service = VehicleService()
        vehicle = vehicle_service.add_a_vehicle(vehicle_reg_no, vehicle_type)
        
        parking_strategy = FirstAvailableParkingStrategy(floor_service.get_floors())
        
        parking_service = ParkingService(parking_strategy)
        parking_spot = parking_service.park_vehicle(vehicle)

        parking_service.unpark_vehicle(vehicle, parking_spot)
    except ParkingSpotUnavailable as e:
        print(f"Parking spot unavailable: {e}")
        return { "error": "Unable to find parking spot" }
    except InvalidVehicleParking as e:
        print(f"Different vehicle parked here: {e}")
        return { "error": "Different vehicle parked here" }        

    
main()