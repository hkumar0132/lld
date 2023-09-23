from models.UserInterface import UserInterface


class NormalUser(UserInterface):
    def __init__(self, id):
        self.id = id
    
    def get_id(self):
        return self.id