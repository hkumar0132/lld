from Factory.VehicleFactory import VehicleFactory

def main():

    vehicle_factory = VehicleFactory().get_vehicle_factory(vehicle_type="ORDINARY")
    vehicle = vehicle_factory.get_vehicle(vehicle="Suzuki")

    vehicle.drive()


if __name__ == "__main__":
    main()