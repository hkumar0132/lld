from abc import ABC, abstractmethod

class IParkingSpotStrategy(ABC):

    @abstractmethod
    def find_parking_spot(self):
        pass