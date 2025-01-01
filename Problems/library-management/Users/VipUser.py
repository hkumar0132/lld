from models.UserInterface import UserInterface


class VipUser(UserInterface):
    def __init__(self, id):
        self.id = id
    
    def get_id(self):
        return self.id