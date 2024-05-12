from Adapter import Adapter
from WeightMachine import WeightMachine

class AdapterImpl(Adapter):

    def __init__(self, weight_machine: WeightMachine) -> None:
        self.weight_machine = weight_machine

    def get_weight_in_kg(self):
        weight_in_pound = self.weight_machine.get_weight_in_pounds() 
        return weight_in_pound * 0.45
