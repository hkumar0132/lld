from IElevator import IElevator
from ElevatorStatus import ElevatorStatus

class Elevator(IElevator):
    def __init__(self, elevator_id) -> None:
        self.elevator_id = elevator_id
        self.status: ElevatorStatus = ElevatorStatus.IDLE

    def set_floor_no(self, floor_no):
        self.floor_no = floor_no

    def get_floor_no(self):
        return self.floor_no
    
    def set_current_status(self, status: ElevatorStatus):
        self.status = status

    def get_current_status(self) -> ElevatorStatus:
        return self.status
    
    def get_elevator_id(self):
        return self.elevator_id
    
    def get_current_status(self):
        return self.status
