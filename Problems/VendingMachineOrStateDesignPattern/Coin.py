from CoinType import CoinType

class Coin:

    def __init__(self, coin: CoinType) -> None:
        self.coin = coin

    def get_value(self):
        return self.coin.value