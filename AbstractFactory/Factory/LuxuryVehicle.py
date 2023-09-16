from Factory.AbstractFactory import AbstractFactory
from Vehicles.BMW import BMW
from Vehicles.Mercedes import Mercedes

class LuxuryVehicle(AbstractFactory):
    def get_vehicle(self, input):
        if input == "BMW":
            return BMW()
        elif input == "MERCEDES":
            return Mercedes()