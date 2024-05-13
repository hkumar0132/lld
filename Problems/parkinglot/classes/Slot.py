class Slot:
    def __init__(self, vehicle_type, slot_id, vehicle=None):
        self.vehicle_type = vehicle_type
        self.slot_id = slot_id
        self.vehicle = vehicle
        
        # print(f'\nAdding {vehicle_type} in slot {slot_id}')
        
    def get_slot_id(self):
        return self.slot_id
        
    def park_vehicle(self, vehicle):
        if vehicle.get_vehicle_type() != self.vehicle_type:
            print('/nInvalid vehicle type for slot')
            return

        self.vehicle = vehicle
        
    def get_vehicle_type(self):
        return self.vehicle_type
        
    def unpark_vehicle(self):
        self.vehicle = None
        
    def get_parked_vehicle(self):
        return self.vehicle
    
    def get_allowed_vehicle_type(self):
        return self.vehicle_type