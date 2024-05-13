from .Vehicle import Vehicle

class NullVehicle(Vehicle):

    def get_tank_capacity(self):
        return 0

    def get_seating_capacity(self):
        return 0
    