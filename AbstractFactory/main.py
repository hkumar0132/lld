from Factory.VehicleFactory import VehicleFactory


def main():
    vehicle = VehicleFactory()
    vehicle_type = vehicle.get_vehicle_type(True)
    v = vehicle_type.get_vehicle("BMW")
    v.drive()

if __name__ == "__main__":
    main()