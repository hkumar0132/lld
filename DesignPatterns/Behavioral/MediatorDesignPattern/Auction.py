from AuctionMediator import AuctionMediator
from Bidder import Bidder

from typing import List

class Auction(AuctionMediator):

    def __init__(self) -> None:
        self.bidders: List[Bidder] = []

    def add_bidder(self, bidder: Bidder):
        self.bidders.append(bidder)

    def place_bid(self, bidder: Bidder, amount: int):
        for b in self.bidders:
            if b.name != bidder.name:
                b.receive_notification(amount)