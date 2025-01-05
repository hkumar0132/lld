from .DriverService import DriverService
from .RiderService import RiderService
from .BillService import BillService
from exceptions.NotFound import NotFoundException
from models.Enums.DriverStatus import DriverStatus

from models.Location import Location
from collections import defaultdict
from threading import Lock
import math

class RideManagementService:
    def __init__(self, driver_service: DriverService, rider_service: RiderService, bill_service: BillService) -> None:
        self.driver_service = driver_service
        self.rider_service = rider_service
        self.bill_service = bill_service
        self.ride_details = defaultdict(list)
        self.ongoing_rides = defaultdict(dict)
        self.ride_lock = Lock()

    def calculate_distance(self, X1, Y1, X2, Y2):
        return math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
        # return abs(X2 - X1) + abs(Y2 - Y1)

    def find_ride(self, username, source: Location, destination: Location):
        drivers = self.driver_service.get_all_drivers()
        rider = self.rider_service.get_rider_by_username(username)

        if not rider:
            raise NotFoundException("Rider not found")
        
        available_rides = []
        for driver in drivers:
            if driver.status != DriverStatus.ACTIVE:
                continue
            distance = self.calculate_distance(
                driver.location.X,
                driver.location.Y,
                source.X,
                source.Y
            )

            if distance <= 5:
                available_rides.append(driver.username)

                self.ride_details[rider.username].append({
                    'source': source,
                    'driver_username': driver.username,
                    'destination': destination
                })
        
        return available_rides

    def choose_ride(self, rider_username, driver_username):

        with self.ride_lock:
            for ride_details in self.ride_details[rider_username]:
                if ride_details['driver_username'] == driver_username:
                    
                    self.ongoing_rides[rider_username] = ride_details
                    self.driver_service.change_driver_status(ride_details['driver_username'], DriverStatus.RESERVED)

                    del self.ride_details[rider_username]

                    print(f'Driver {driver_username} chosen by rider {rider_username}')
                    return

        raise NotFoundException("driver not available")
        
    def end_ride(self, rider_username):
        current_ride = self.ongoing_rides[rider_username]
        if not current_ride:
            raise NotFoundException("No ongoing rides to end")
        
        distance = self.calculate_distance(
            current_ride['source'].X,
            current_ride['source'].Y,
            current_ride['destination'].X,
            current_ride['destination'].Y
        )
        
        self.bill_service.calculate_bill(rider_username, current_ride['driver_username'], distance)
        self.rider_service.update_rider_location(rider_username, current_ride['destination'])
        self.driver_service.update_driver_location(current_ride['driver_username'], current_ride['destination'])
        self.driver_service.change_driver_status(current_ride['driver_username'], DriverStatus.ACTIVE)

        del self.ongoing_rides[rider_username]

        print("Ride ended")