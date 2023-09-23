class Ticket:
    def __init__(self, parking_lot_id, floor_id, slot_id):
        self.parking_lot_id = parking_lot_id
        self.floor_id = floor_id
        self.slot_id = slot_id
        
    def get_ticket_id(self):
        return f'{self.parking_lot_id}_{self.floor_id}_{self.slot_id}'