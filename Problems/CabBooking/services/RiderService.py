from models.User import User
from models.Rider import Rider
from models.Location import Location
from exceptions.DuplicateUsername import DuplicateUsernameException
from exceptions.NotFound import NotFoundException
from models.Enums.Gender import Gender

class RiderService:
    def __init__(self) -> None:
        self.riders: list[Rider] = []

    def add_user(self, username, name, age, gender: Gender):
        for riders in self.riders:
            if riders.username == username:
                raise DuplicateUsernameException('Username already exists')
        
        user = User(username, name, age, gender)

        rider = Rider(user)
        self.riders.append(rider)

        print("Rider added")
        return rider
    
    def update_user(self, username, updated_details: User):
        for rider in self.riders:
            if rider.username == username:
                if (updated_details.name):
                    rider.update_name(updated_details.name)
                if (updated_details.age):
                    rider.update_age(updated_details.age)
                if (updated_details.gender):
                    rider.update_gender(updated_details.gender)
                print("rider details updated")
                return
        
        raise NotFoundException('Rider not found')
        
    def update_rider_location(self, username, location: Location):
        for rider in self.riders:
            if rider.username == username:
                rider.update_rider_location(location)
                print("Rider locaition updated")
                return
        
        raise NotFoundException('Rider not found')
        
    def get_rider_by_username(self, username) -> Rider:
        for rider in self.riders:
            if rider.username == username:
                return rider