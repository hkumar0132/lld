import uuid

class User:

    def __init__(self, name, email) -> None:
        self.user_id = uuid.uuid4()
        self.name = name
        self.email = email

    def update_name(self, name):
        self.name = name