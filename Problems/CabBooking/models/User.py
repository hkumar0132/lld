from .Location import Location
class User:
    def __init__(self, username, name, age, gender, location=None) -> None:
        self.username = username
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location

    def update_name(self, name):
        self.name = name

    def update_age(self, age):
        self.age = age

    def update_gender(self, gender):
        self.gender = gender

    def update_location(self, location: Location):
        self.location = location