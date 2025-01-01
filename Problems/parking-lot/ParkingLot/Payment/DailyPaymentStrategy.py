from IPaymentStrategy import IPaymentStrategy

class DailyPaymentStrategy(IPaymentStrategy):
    
    def calculate_parking_charge(self, vehicle_type, exit_time):
        # Charges based on number of days
        return 1000        