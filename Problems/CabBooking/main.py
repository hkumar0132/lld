from services.DriverService import DriverService
from services.BillService import BillService
from services.RideManagementService import RideManagementService
from services.RiderService import RiderService

from models.Enums.Gender import Gender
from models.Enums.VehicleTypes import VehicleTypes
from models.Enums.DriverStatus import DriverStatus

from models.Location import Location

def main():
    rider_service = RiderService()
    rider_service.add_user(
        "1",
        "Himanshu",
        24,
        Gender.MALE
    )
    rider_service.update_rider_location("1", Location(0, 0))

    rider_service.add_user(
        "2",
        "Anshu",
        19,
        Gender.MALE
    )
    rider_service.update_rider_location("1", Location(10, 0))

    rider_service.add_user(
        "3",
        "K",
        32,
        Gender.FEMALE
    )
    rider_service.update_rider_location("1", Location(15, 6))

    driver_service = DriverService()
    driver_service.add_driver(
        "1",
        "Driver1",
        22,
        Gender.MALE,
        VehicleTypes.CAR,
        "Swift, KA-01-12345",
        "ABC122",
        Location(10, 1)
    )

    driver_service.add_driver(
        "2",
        "Driver2",
        29,
        Gender.MALE,
        VehicleTypes.CAR,
        "Swift, KA-01-12345",
        "ABC123",
        Location(11, 10)
    )

    driver_service.add_driver(
        "3",
        "Driver3",
        24,
        Gender.MALE,
        VehicleTypes.CAR,
        "Swift, KA-01-12345",
        "ABC125",
        Location(5, 3)
    )

    bill_service = BillService(driver_service)

    ride_management_service = RideManagementService(
        driver_service,
        rider_service,
        bill_service
    )

    rides = ride_management_service.find_ride(
        "1" ,
        Location(0,0),
        Location(20,1)
    )

    print("RIDES: ", rides)

    rides = ride_management_service.find_ride("2" ,Location(10,0), Location(15,3))
    print("RIDES: ", rides)

    ride_management_service.choose_ride("2", "1")

    ride_management_service.end_ride("2")

    driver_service.change_driver_status("1", DriverStatus.INACTIVE)

    rides = ride_management_service.find_ride("3", Location(15,6), Location(20,4))
    print("RIDES: ", rides)

    bill_service.find_total_earning()

if __name__ == "__main__":
    main()