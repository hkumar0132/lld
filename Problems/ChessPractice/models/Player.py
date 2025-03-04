class Player:
    def __init__(self, player_id, name, email) -> None:
        self.player_id = player_id
        self.name = name
        self.email = email

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email