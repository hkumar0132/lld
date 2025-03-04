from .User import User
from enums.UserTier import UserTier

class PlatinumTierUser(User):
    def __init__(self, user_id, name, email, mobile_no, country) -> None:
        super().__init__(user_id, name, email, mobile_no, country, UserTier.PLATINUM)
        points_multiplier = 2
        free_checkout = True
        minimum_redemption_point = 40
        self.exclusive_offers = []

    def get_dedicated_support(self):
        pass

    def get_exclusive_offers(self):
        pass