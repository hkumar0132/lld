from Room import Room
from RoomVisitor import RoomVisitor

class SingleRoom(Room):

    def accept(self, visitor: RoomVisitor):
        visitor.visit_single_room(self)