from IPaymentStrategy import IPaymentStrategy

class HourlyPaymentStrategy(IPaymentStrategy):
    
    def calculate_parking_charge(self, vehicle_type, hours):
        # Charges based on number of hours
        return 100
        