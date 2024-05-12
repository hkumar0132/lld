from RoomVisitor import RoomVisitor
from Room import SingleRoom, DoubleRoom, DeluxeRoom

class RoomPriceVisitor(RoomVisitor):
    def visit_single_room(self, room: SingleRoom):
        room.room_price = 1000

    def visit_double_room(self, room: DoubleRoom):
        room.room_price = 2500

    def visit_deluxe_room(self, room: DeluxeRoom):
        room.room_price = 5000