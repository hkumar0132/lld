from ..models.User import User

class UserService:
    def __init__(self) -> None:
        self.users : list[User] = []

    def get_user_room_ids(self):
        pass

    def add_user(self, user_id):
        pass

    def remove_user(self, user_id):
        pass

    def add_room_id(self, user_id, room_id):
        pass

    def remove_room_id(self, user_id, room_id):
        pass