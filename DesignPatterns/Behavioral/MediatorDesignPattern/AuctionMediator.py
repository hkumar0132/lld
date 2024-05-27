from abc import ABC, abstractmethod

class AuctionMediator(ABC):

    @abstractmethod
    def add_bidder():
        pass

    @abstractmethod
    def place_bid():
        pass