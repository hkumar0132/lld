from AuctionMediator import AuctionMediator

class Bidder:
    def __init__(self, name: str, mediator: AuctionMediator) -> None:
        self.name = name
        self.mediator = mediator
        self.mediator.add_bidder(self)

    def place_bid(self, amount: int):
        self.mediator.place_bid(self, amount)

    def receive_notification(self, amount):
        print(f"Nofication received by {self.name} for {amount}")

    @property
    def get_name(self):
        return self.name