from ParkingLot import ParkingLot
from models.VehicleType import VehicleType

def _validate_vehicle_type(vehicle_type):
    print('vehicle_type: ', vehicle_type)
    if vehicle_type == 'CAR':
        return VehicleType.CAR
    elif vehicle_type == 'BIKE':
        return VehicleType.BIKE
    elif vehicle_type == 'TRUCK':
        return  VehicleType.TRUCK
        
    raise Exception('\nInvalid vehicle type')

def main():
    
    # parking_lot = ParkingLot("PR1234", 2, 6)
    # parking_lot.park_vehicle(VehicleType.CAR, "KA-01-DB-1234", 'Black')
    # parking_lot.unpark_vehicle("PR1234_0_3")
    # parking_lot.unpark_vehicle("PR1234_1_3")

    
    print('\nWaiting for commands....')
    i = ""
    parking_lot = None
    
    while True:
        i = input()
        if i == 'exit':
            break
        i = i.split(' ')
        
        if i[0] == 'create_parking_lot':
            parking_lot_id = i[1]
            no_of_floors = int(i[2])
            no_of_slots_per_floor = int(i[3])
            parking_lot = ParkingLot(parking_lot_id, no_of_floors, no_of_slots_per_floor)
        elif i[0] == 'park_vehicle' and parking_lot:
            vehicle_type = _validate_vehicle_type(i[1])
            reg_no = i[2]
            color = i[3]
            parking_lot.park_vehicle(vehicle_type, reg_no, color)
            
        elif i[0] == 'unpark_vehicle' and parking_lot:
            ticket_id = i[1]
            parking_lot.unpark_vehicle(ticket_id)
        elif i[0] == 'display' and parking_lot:
            vehicle_type = _validate_vehicle_type(i[2])
            display_type = i[1]
            if display_type == 'free_count':
                parking_lot.get_number_of_free_slots_per_floor(vehicle_type)
            elif display_type == 'free_slots':
                parking_lot.get_free_slots_per_floor(vehicle_type)
            elif display_type == 'occupied_slots':
                parking_lot.get_occupied_slots(vehicle_type)
            else:
                print('\nInvalid input')
                break
        else:
            print('\nInvalid input')
            break

if __name__ == "__main__":
    main()