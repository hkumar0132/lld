from classes.Floor import Floor
from classes.Ticket import Ticket
from models.VehicleFactory import VehicleFactory


class ParkingLot:
    def __init__(self, parking_lot_id, number_of_floors, number_of_slots_per_floor):
        '''
        {
            0: {},
            1: {},
            2: {}
        }
        '''
        self.parking_lot_id = parking_lot_id
        self.floors = []
        self.number_of_floors = number_of_floors
        self.number_of_slots_per_floor = number_of_slots_per_floor
        self.tickets = {}
        self.create_parking_lot()
        
    def create_parking_lot(self):
        for i in range(0, self.number_of_floors):
            self.add_floor()
            
        print(f'Created parking lot with {self.number_of_floors} floors and {self.number_of_slots_per_floor} slots per floor')
        
    def add_floor(self):
        floor = Floor(self.number_of_slots_per_floor, len(self.floors))
        self.floors.append(floor)
    
    def park_vehicle(self, vehicle_type, registration_no, color):
        vehicle = VehicleFactory().get_vehicle(vehicle_type, registration_no, color)
        # print('park vehicle: ', vehicle)
        
        for floor in self.floors:
            for slot in floor.get_free_slots(vehicle_type):
                if slot.get_allowed_vehicle_type() == vehicle_type:
                    floor.park_vehicle_to_slot(slot, vehicle)
                    slot_id = slot.get_slot_id()
                    floor_id = floor.get_floor_id()
                    ticket_id = Ticket(self.parking_lot_id, floor_id, slot_id).get_ticket_id()
                    if ticket_id in self.tickets:
                        print('Duplicate ticket id')
                        return
                    self.tickets[ticket_id] = { 'vehicle': vehicle, 'slot_id': slot, 'floor_id': floor }
                    print(f'Parked vehicle. Ticket ID: {ticket_id}')
                    return
                    
        print('\nParking Lot Full')
    
    def unpark_vehicle(self, ticket_id):
        if ticket_id not in self.tickets:
            print('\nInvalid Ticket')
            return None
        vehicle_detail = self.tickets[ticket_id]
        vehicle = vehicle_detail['vehicle']
        slot = vehicle_detail['slot_id']
        floor = vehicle_detail['floor_id']
        floor.unpark_vehicle_from_slot(slot)
        del self.tickets[ticket_id]
        print(f'Unparked vehicle with Registration Number: {vehicle.get_registration_no()} and Color: {vehicle.get_vehicle_color()}')
    
    def get_number_of_free_slots_per_floor(self, vehicle_type):
        for floor in self.floors:
            free_slots = floor.get_free_slots(vehicle_type)
            print(f'No. of free slots for {vehicle_type} on Floor {floor.get_floor_id()}: {len(free_slots)}')
        
    def get_free_slots_per_floor(self, vehicle_type):
        for floor in self.floors:
            free_slots = floor.get_free_slots(vehicle_type)
            comma_separated_values_of_slot_nos = ""
            for slot in free_slots:
                comma_separated_values_of_slot_nos += str(slot.get_slot_id()) + ", "
            print(f'Free slots for {vehicle_type} on Floor {floor.get_floor_id()}: {comma_separated_values_of_slot_nos}')
    
    def get_occupied_slots(self, vehicle_type):
        for floor in self.floors:
            free_slots = floor.get_occupied_slots(vehicle_type)
            comma_separated_values_of_slot_nos = ""
            for slot in free_slots:
                comma_separated_values_of_slot_nos += str(slot.get_slot_id()) + ", "
            print(f'Occupied slots for f{vehicle_type} on Floor {floor.get_floor_id()}: {comma_separated_values_of_slot_nos}')