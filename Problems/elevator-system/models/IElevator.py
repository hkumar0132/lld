from abc import ABC, abstractmethod
from ElevatorStatus import ElevatorStatus

class IElevator(ABC):
    
    @abstractmethod
    def set_floor_no(self, floor_no):
        pass

    @abstractmethod
    def get_floor_no(self):
        pass
    
    @abstractmethod
    def set_current_status(self, status: ElevatorStatus):
        pass

    @abstractmethod
    def get_current_status(self) -> ElevatorStatus:
        pass
    
    @abstractmethod
    def get_elevator_id(self):
        pass
    