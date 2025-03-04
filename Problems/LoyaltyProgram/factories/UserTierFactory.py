from enums.UserTier import UserTier
from models.GoldTierUser import GoldTierUser
from models.SilverTierUser import SilverTierUser
from models.PlatinumTierUser import PlatinumTierUser

class UserTierFactory:

    def get_user_based_on_tier(self, user_details, tier):
        if tier == UserTier.SILVER:
            return SilverTierUser(user_details)
        elif tier == UserTier.GOLD:
            return GoldTierUser(user_details)
        elif tier == UserTier.PLATINUM:
            return PlatinumTierUser(user_details)
        