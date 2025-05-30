from enums.UserType import UserType
from models.Owner import Owner
from models.Member import Member

class UserFactory:

    def get_user_by_type(user_details, user_type: UserType):
        if user_type == UserType.OWNER:
            return Owner(user_details)
        elif user_type == UserType.MEMBER:
            return Member(user_details)
        
        raise Exception('User type does not exists')