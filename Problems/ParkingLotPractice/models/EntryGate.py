from threading import Lock

class EntryGate:
    def __init__(self, id) -> None:
        self.id = id
        self.parking_tickets = []
        self.lock = Lock()

    def __add_parking_ticket(self, parking_ticket):
        self.parking_tickets.append(parking_ticket)

    def enter_vehicle(self, parking_ticket):
        with self.lock:
            self.__add_parking_ticket(parking_ticket)