from VehicleFactory import VehicleFactory
from VehicleFactory import Vehicle

class Client:

    vehicle_factory = VehicleFactory()

    bike = vehicle_factory.get_vehicle("bike")
    print("seating: ", bike.get_seating_capacity(), " tank: ", bike.get_tank_capacity())

    truck = vehicle_factory.get_vehicle("truck")
    # Without the null object, this would throw error
    print("seating: ", truck.get_seating_capacity(), " tank: ", truck.get_tank_capacity())