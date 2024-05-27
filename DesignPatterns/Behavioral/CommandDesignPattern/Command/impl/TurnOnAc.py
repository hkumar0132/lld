from Command import ICommand
from AirConditioner import AirConditioner

class TurnOnAc(ICommand):

    def __init__(self, air_conditioner: AirConditioner) -> None:
        self.ac = air_conditioner

    def execute(self):
        self.ac.turn_on_ac()