from typing import List

from IExternalButtonDispatcher import IExternalButtonDispatcher
from ElevatorManager import ElevatorManager

class OddEvenExternalButtonDispatcher(IExternalButtonDispatcher):

    def __init__(self, elevator_managers) -> None:
        self.elevator_managers: List[ElevatorManager] = elevator_managers

    def dispatch(self, floor_no, direction):
        for elevator_manager in self.elevator_managers:
            if floor_no % 2 == 1 and elevator_manager.get_elevator_id() % 2 == 1:
                return elevator_manager.request_elevator(floor_no, direction)
            elif floor_no % 2 == 0 and elevator_manager.get_elevator_id() % 2 == 0:
                return elevator_manager.request_elevator(floor_no, direction)
        raise Exception("Unable to submit request")