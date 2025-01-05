from .DriverService import DriverService
from constants import PRICE_PER_UNIT_DISTANCE

from collections import defaultdict

class BillService:
    def __init__(self, driver_service: DriverService) -> None:
        self.driver_service = driver_service
        self.total_bill = defaultdict(list)

    def __calculate_fare(self, distance):
        return round(PRICE_PER_UNIT_DISTANCE * distance)

    def calculate_bill(self, rider_username, driver_username, distance):
        bill = self.__calculate_fare(distance)
        self.total_bill[rider_username].append({
            'distance': distance,
            'bill': bill,
            'driver_username': driver_username
        })

        print(f"Bill amount: {bill}")

    def find_total_earning(self):
        earning_by_drivers = defaultdict(int)
        for rider_username in self.total_bill.keys():
            for bill_details in self.total_bill[rider_username]:
                earning_by_drivers[bill_details['driver_username']] += bill_details['bill']
        
        for driver_username in earning_by_drivers.keys():
            print(f"Driver {driver_username} ${earning_by_drivers[driver_username]}")