from Vehicle.SportsVehicle import SportsVehicle
from Vehicle.NormalVehicle import NormalVehicle

def main():
    print('executing')
    normal_vehicle = NormalVehicle()
    normal_vehicle.drive()
    
    special_vehicle = SportsVehicle()
    special_vehicle.drive()

if __name__ == "__main__":
    main()