from exceptions.NotFoundException import NotFoundException
class ParkingFloor:
    def __init__(self, id, parking_spots) -> None:
        self.id = id
        self.parking_spots = parking_spots

    def get_available_parking_spots(self):
        pass

    def park_vehicle(self, vehicle):
        for spot in self.parking_spots:
            parked = spot.park_vehicle(vehicle)
            if parked:
                return spot.id
            
    def unpark_vehicle(self, parking_spot_id, vehicle):
        for spot in self.parking_spots:
            if spot.id == parking_spot_id:
                spot.unpark_vehicle(vehicle)
                return spot.id

    def add_parking_spot(self, parking_spot):
        self.parking_spots.append(parking_spot)

    def get_parking_spots(self):
        return self.parking_spots