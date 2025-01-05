from models.User import User
from models.Vehicle import Vehicle
from exceptions.DuplicateException import DuplicateException
from models.Enums.VehicleTypes import VehicleTypes
from exceptions.NotFoundException import NotFoundException

class UserManagementService:
    def __init__(self) -> None:
        self.users: list[User] = []
        
    def add_user(self, id, name, age, gender):
        for user in self.users:
            if user.id == id:
                raise DuplicateException('User id already exists')
        self.users.append(User(id, name, age, gender))

    def add_vehicle(self, user_id, vehicle_type: VehicleTypes, reg_no):
        for user in self.users:
            if user.id == user_id:
                vehicle = Vehicle(vehicle_type, reg_no)
                user.add_vehicle(vehicle)
                break

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        raise NotFoundException("User not found")