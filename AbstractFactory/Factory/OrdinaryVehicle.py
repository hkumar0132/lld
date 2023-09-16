from Factory.AbstractFactory import AbstractFactory
from Vehicles.XUV import XUV
from Vehicles.Suzuki import Suzuki

class OrdinaryVehicle(AbstractFactory):
    def get_vehicle(self, input):
        if input == "SUZUKI":
            return Suzuki()
        elif input == "XUV":
            return XUV()