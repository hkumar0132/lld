from RoomVisitor import RoomVisitor
from Room import SingleRoom, DoubleRoom, DeluxeRoom

class RoomReserveVisitor(RoomVisitor):
    def visit_single_room(self, room: SingleRoom):
        print("Single room reserve")

    def visit_double_room(self, room: DoubleRoom):
        print("Double room reserve")

    def visit_deluxe_room(self, room: DeluxeRoom):
        print("Deluxe room reserve")
