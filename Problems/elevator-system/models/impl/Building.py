from typing import List

from Floor import Floor

class Building:
    def __init__(self, floors) -> None:
        self.floors: List[Floor] = floors

    def request_elevator(self, floor_no):
        if floor_no >= len(self.floors):
            raise Exception("Floor does not exist")
        self.floors[floor_no].request_elevator()