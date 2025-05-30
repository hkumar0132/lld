from .User import User
from enums.UserTier import UserTier

class SilverTierUser(User):
    def __init__(self, user_id, name, email, mobile_no, country) -> None:
        super().__init__(user_id, name, email, mobile_no, country, UserTier.SILVER)
        points_multiplier = 1.1
        free_checkout = False
        minimum_redemption_point = 100
