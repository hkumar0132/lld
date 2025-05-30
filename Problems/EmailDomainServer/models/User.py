class User:
    def __init__(self, user_id, name, mobile_no, country, user_type) -> None:
        self.user_id = user_id
        self.user_type = user_type
        self.name = name
        self.mobile_no = mobile_no
        self.country = country