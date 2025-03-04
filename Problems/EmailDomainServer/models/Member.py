from enums.UserType import UserType

class Member:
    def __init__(self, user_id, name, mobile_no, country) -> None:
        super().__init__(user_id, name, mobile_no, country, UserType.Member)