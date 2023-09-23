from abc import ABC, abstractclassmethod

class FloorInterface(ABC):
    def __init__(self, number_of_slots, floor_id):
        self.number_of_slots = number_of_slots
        self.floor_id = floor_id
        self.slots = []
    
    @abstractclassmethod
    def add_slots_to_floor(self, number_of_slots):
        pass
    
    @abstractclassmethod    
    def get_floor_id(self):
        pass
    
    @abstractclassmethod
    def _assign_vehicle_type_to_slot_logic(self):
        pass
        
    @abstractclassmethod
    def add_slot_to_floor(self):
        pass
        
    @abstractclassmethod
    def get_free_slots(self, vehicle_type):
        pass
    
    @abstractclassmethod
    def get_occupied_slots(self, vehicle_type):
        pass
    
    @abstractclassmethod
    def park_vehicle_to_slot(self, slot, vehicle):
        pass
        
    @abstractclassmethod
    def unpark_vehicle_from_slot(self, slot):
        pass