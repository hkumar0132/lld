from .Vehicle import Vehicle

class User:
    def __init__(self, id, name, age, gender, vehicles: list[Vehicle] = []) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.vehicles = vehicles

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def get_vehicles(self) -> list[Vehicle]:
        return self.vehicles