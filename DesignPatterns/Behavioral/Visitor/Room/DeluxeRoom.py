from Room import Room
from RoomVisitor import RoomVisitor

class DeluxeRoom(Room):

    def accept(self, visitor: RoomVisitor):
        visitor.visit_deluxe_room(self)