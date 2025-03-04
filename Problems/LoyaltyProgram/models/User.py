class User:
    def __init__(self, user_id, name, email, mobile_no, country, tier, hashed_password) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile_no = mobile_no
        self.country = country
        self.tier = tier
        self.hashed_password = hashed_password

    def update_tier(self, tier):
        self.tier = tier

    def update_name(self, name):
        self.name = name
