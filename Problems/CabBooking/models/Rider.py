from .Location import Location
from .Enums.Gender import Gender
from .User import User

class Rider(User):

    def __init__(self, user_detail: User):
        super().__init__(user_detail.username, user_detail.name, user_detail.age, user_detail.gender, user_detail.location)

    def update_rider(username, updated_details):
        if (updated_details.name):
            super().update_name(updated_details.name)
        if (updated_details.age):
            super().update_age(updated_details.age)
        if (updated_details.gender):
            super().update_gender(updated_details.gender)

    def update_rider_location(self, current_location: Location):
        super().update_location(current_location)
