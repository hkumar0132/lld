from Room import Room
from RoomVisitor import RoomVisitor

class DoubleRoom(Room):

    def accept(self, visitor: RoomVisitor):
        visitor.visit_double_room(self)