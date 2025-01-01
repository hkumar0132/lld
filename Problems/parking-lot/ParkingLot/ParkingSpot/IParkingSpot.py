from abc import ABC, abstractmethod

class IParkingSpot(ABC):
    def __init__(self) -> None:
        self.is_occupied = False

    @abstractmethod
    def park_vehicle():
        pass

    @abstractmethod
    def unpark_vehicle():
        pass