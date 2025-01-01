from abc import ABC, abstractmethod

class IParkingSpotManager(ABC):
    
    def __init__(self, parking_spots) -> None:
        self.parking_spots = parking_spots
    
    @abstractmethod
    def add_parking_spot(self):
        pass

    @abstractmethod
    def remove_parking_spot(self):
        pass

    @abstractmethod
    def find_parking_spot(self):
        pass

    @abstractmethod
    def park_vehicle(self):
        pass

    @abstractmethod
    def unpark_vehicle(self):
        pass