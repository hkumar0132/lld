from IParkingSpotStrategy import IParkingSpotStrategy

class FourWheelerParkingSpot:
    def __init__(self, parking_strategy: IParkingSpotStrategy) -> None:
        self.parking_strategy = parking_strategy

    def park_vehicle(self):
        self.parking_strategy.find_parking_spot()

    def unpark_vehicle():
        pass