class Vehicle:
    def __init__(self, vehicle_type, registration_no, color):
        self.vehicle_type = vehicle_type
        self.registration_no = registration_no
        self.color = color
        
    def get_registration_no(self):
        return self.registration_no

    def get_vehicle_type(self):
        return self.vehicle_type
    
    def get_vehicle_color(self):
        return self.color