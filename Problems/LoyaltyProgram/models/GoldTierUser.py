from .User import User
from enums.UserTier import UserTier

class GoldTierUser(User):
    def __init__(self, user_id, name, email, mobile_no, country) -> None:
        super().__init__(user_id, name, email, mobile_no, country, UserTier.GOLD)
        points_multiplier = 1.5
        free_checkout = True
        minimum_redemption_point = 70
        self.exclusive_offers = []

    def get_dedicated_support(self):
        pass

    def get_exclusive_offers(self):
        pass