from PayToFriend import PayToFriend
from PayToMerchant import PayToMerchant

class Client:

    pay_to_friend = PayToFriend()
    pay_to_merchant = PayToMerchant()

    pay_to_friend.send_money()
    pay_to_merchant.send_money()