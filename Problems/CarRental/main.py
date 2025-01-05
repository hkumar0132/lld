from services.UserManagementService import UserManagementService
from services.RideManagementService import RideManagementService

from models.Enums.Gender import Gender
from models.Enums.VehicleTypes import VehicleTypes

def main():
    ums = UserManagementService()

    ums.add_user("1", "Rohan", 36, Gender.MALE) 
    ums.add_vehicle("1", VehicleTypes.SWIFT, "KA-01-12345")

    ums.add_user("2", "Shashank", 29, Gender.MALE)
    ums.add_vehicle("2", VehicleTypes.BALENO, "TS-05-62395")

    ums.add_user("3", "Nandini", 29, Gender.FEMALE)

    ums.add_user("4", "Shipra", 27, Gender.FEMALE)
    ums.add_vehicle("4", VehicleTypes.POLO, "KA-05-41491")
    ums.add_vehicle("4", VehicleTypes.ACTIVA, "KA-12-12332")

    ums.add_user("5", "Gaurav", 29, Gender.MALE)

    ums.add_user("6", "Rahul", 35, Gender.MALE)
    ums.add_vehicle("6", VehicleTypes.XUV, "KA-05-1234")

    rms = RideManagementService(ums)

    rms.offer_ride("1", "Hyderabad", 1, VehicleTypes.SWIFT, "KA-01-12345", "Bangalore")
    
    rms.offer_ride("4", "Bangalore", 1, VehicleTypes.ACTIVA, "KA-12-12332", "Mysore")

    rms.offer_ride("4", "Bangalore", 2, VehicleTypes.POLO, "KA-05-41491", "Mysore")

    rms.offer_ride("2", "Hyderabad", 2, VehicleTypes.BALENO, "TS-05-62395", "Bangalore")

    rms.offer_ride("6", "Hyderabad", 5, VehicleTypes.XUV, "KA-05-1234", "Bangalore")

    rms.offer_ride("1", "Bangalore", 1, VehicleTypes.SWIFT, "KA-01-12345", "Pune")
    
    rms.select_ride("3", "Bangalore", "Mysore", 1, "Most Vacant")
    rms.select_ride("5", "Bangalore", "Mysore", 1, "Preferred Vehicle", VehicleTypes.ACTIVA)
    rms.select_ride("2", "Mumbai", "Bangalore",1, "Most Vacant")
    rms.select_ride("1", "Hyderabad", "Bangalore", 1, "Preferred Vehicle", VehicleTypes.BALENO)
    rms.select_ride("2", "Hyderabad", "Bangalore", 1, "Preferred Vehicle", VehicleTypes.POLO)

    rms.end_ride("3")
    rms.end_ride("5")
    rms.end_ride("1")
    rms.end_ride("2")

    rms.print_ride_stats()

if __name__ == "__main__":
    main()