from Auction import Auction
from Bidder import Bidder

class Client:

    auction = Auction()

    bidder1 = Bidder("Himanshu", auction)
    bidder2 = Bidder("ABC", auction)

    bidder1.place_bid(10000)
    bidder2.place_bid(20000)