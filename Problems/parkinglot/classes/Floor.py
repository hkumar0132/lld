from classes.Slot import Slot
from models.FloorInterface import FloorInterface
from models.VehicleType import VehicleType


class Floor(FloorInterface):
    def __init__(self, number_of_slots, floor_id):
        self.number_of_slots = number_of_slots
        self.floor_id = floor_id
        self.slots = []
        
        self.add_slots_to_floor(number_of_slots)
        
    def add_slots_to_floor(self, number_of_slots):
        for i in range(0, number_of_slots):
            self.add_slot_to_floor()
        
    def get_floor_id(self):
        return self.floor_id
        
    def _assign_vehicle_type_to_slot_logic(self):
        if len(self.slots) == 0:
            return VehicleType.TRUCK
        elif len(self.slots) < 3:
            return VehicleType.BIKE
        else:
            return VehicleType.CAR
        
    def add_slot_to_floor(self):
        new_slot = Slot(self._assign_vehicle_type_to_slot_logic(), len(self.slots))
        self.slots.append(new_slot)
        
    def get_free_slots(self, vehicle_type):
        free_slots = []
        for slot in self.slots:
            if slot.get_parked_vehicle() == None and slot.get_vehicle_type() == vehicle_type:
                free_slots.append(slot)
        return free_slots
    
    def get_occupied_slots(self, vehicle_type):
        free_slots = []
        for slot in self.slots:
            if slot.get_parked_vehicle() != None and slot.get_vehicle_type() == vehicle_type:
                free_slots.append(slot)
        return free_slots
    
    def park_vehicle_to_slot(self, slot, vehicle):
        slot.park_vehicle(vehicle)
        
    def unpark_vehicle_from_slot(self, slot):
        slot.unpark_vehicle()