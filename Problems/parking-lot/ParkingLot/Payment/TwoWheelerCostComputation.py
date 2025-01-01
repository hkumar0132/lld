from ICostComputation import ICostComputation
from IPaymentStrategy import IPaymentStrategy

class TwoWheelerCostComputation(ICostComputation):

    def __init__(self, cost_calculation_strategy: IPaymentStrategy) -> None:
        self.cost_calculation_strategy = cost_calculation_strategy
    
    def calculate_charges():
        # Charges based on cost_calculation_strategy and vehicle type
        pass