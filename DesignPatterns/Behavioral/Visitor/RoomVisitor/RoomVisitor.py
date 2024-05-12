from abc import ABC

from Room import Room

class RoomVisitor(ABC):
    def visit_single_room(self, element: Room):
        pass

    def visit_double_room(self, element: Room):
        pass

    def visit_deluxe_room(self, element: Room):
        pass