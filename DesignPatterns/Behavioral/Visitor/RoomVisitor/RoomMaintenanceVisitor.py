from RoomVisitor import RoomVisitor
from Room import SingleRoom, DoubleRoom, DeluxeRoom

class RoomMaintenanceVisitor(RoomVisitor):
    def visit_single_room(self, room: SingleRoom):
        print("Single room maintenance")

    def visit_double_room(self, room: DoubleRoom):
        print("Double room maintenance")

    def visit_deluxe_room(self, room: DeluxeRoom):
        print("Deluxe room maintenance")
