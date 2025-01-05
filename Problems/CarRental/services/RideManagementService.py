from models.User import User
from models.Vehicle import Vehicle
from .UserManagementService import UserManagementService
from exceptions.NotFoundException import NotFoundException
from exceptions.NotAvailableException import NotAvailableException
from models.Enums.VehicleStatus import VehicleStatus

from collections import defaultdict

class RideManagementService:
    def __init__(self, user_service: UserManagementService) -> None:
        self.user_service = user_service
        self.offered_rides = []
        self.selected_rides = defaultdict(dict)

    def offer_ride(self, user_id, origin, available_seats, vehicle_type, reg_no, destination):
        try:
            user = self.user_service.get_user_by_id(user_id)
            vehicles = user.get_vehicles()

            for vehicle in vehicles:
                if vehicle.reg_no == reg_no:
                    if vehicle.status != VehicleStatus.AVAILABLE:
                        raise NotAvailableException("Vehicle not available")
                    
                    vehicle.change_vehicle_status(VehicleStatus.OFFERED)
                    self.offered_rides.append({
                        'user_id': user_id,
                        'vehicle': vehicle,
                        'origin': origin,
                        'destination': destination,
                        'available_seats': available_seats,
                        'reg_no': reg_no
                    })

                    print("Vehicle available for ride")
                    break
        except NotAvailableException as e:
            print(e)
    
    def __most_vacant_ride(self, possible_rides):
        max_av_seats = 0
        selected_ride = None
        for ride in possible_rides:
            if ride['available_seats'] > max_av_seats:
                max_av_seats = ride['available_seats']
                selected_ride = ride
        return selected_ride

    def __preferred_vehicle_ride(self, possible_rides, vehicle_type):
        for ride in possible_rides:
            if ride['vehicle'].type == vehicle_type:
                return ride
    
    def select_ride(self, user_id, origin, destination, seats_required, algorithm="Most Vacant", preferred_vehicle=None):
        try:
            possible_rides = []
            for ride in self.offered_rides:
                if ride['origin'] == origin and ride['destination'] == destination and seats_required <= ride['available_seats']:
                    possible_rides.append(ride)
            
            if len(possible_rides) == 0:
                raise NotFoundException("No offered rides")

            ride = None
            if algorithm == "Most Vacant":
                ride = self.__most_vacant_ride(possible_rides)
            elif algorithm == "Preferred Vehicle":
                ride = self.__preferred_vehicle_ride(possible_rides, preferred_vehicle)
            else:
                raise NotFoundException("Vehicle selection strategy does not exist")

            if not ride:
                raise NotFoundException("No rides found")
            self.selected_rides[user_id] = {
                'ride': ride,
                'status': 'started'
            }
            print(f"Selected ride: {ride['reg_no']}")
            ride['vehicle'].change_vehicle_status(VehicleStatus.RESERVED)
            return ride
        except NotFoundException as e:
            print(e)

    def end_ride(self, user_id):
        try:
            for user_id_key in self.selected_rides.keys():
                if user_id_key == user_id:
                    self.selected_rides[user_id_key]['status'] = 'ended'
                    self.selected_rides[user_id_key]['ride']['vehicle'].change_vehicle_status(VehicleStatus.AVAILABLE)
                    print(f"Ride ended for {user_id}")
                    return
            raise NotFoundException("Ride not found, cannot end")
        except NotFoundException as e:
            print(e)

    def print_ride_stats(self):
        stats = defaultdict(lambda: { 'offered': 0, 'taken': 0 })

        for offered in self.offered_rides:
            stats[offered['user_id']]['offered'] += 1
        
        for user_id_key in self.selected_rides.keys():
            stats[user_id_key]['taken'] += ( 1 if self.selected_rides[user_id_key]['status'] == 'ended' else 0 )
        
        for user_id in stats.keys():
            user = self.user_service.get_user_by_id(user_id)
            print(f"{user.name}: {stats[user_id]['taken']} taken, {stats[user_id]['offered']} offered")