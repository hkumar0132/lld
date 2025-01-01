from heapq import heappush, heappop

from IElevator import IElevator
from Direction import Direction

class ElevatorManager:
    def __init__(self, elevator: IElevator):
        self.elevator = elevator
        self.request_up_min_heap = []
        self.request_down_max_heap = []

    def get_elevator_id(self) -> IElevator:
        return self.elevator.get_elevator_id()
    
    def request_elevator(self, floor_no, direction):
        if self.elevator.get_floor_no() == floor_no:
            return True
        
        if direction == Direction.UP:
            heappush(self.request_up_min_heap, -floor_no)
        else:
            heappop(self.request_down_max_heap, floor_no)