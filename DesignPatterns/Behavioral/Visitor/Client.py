from Room import SingleRoom, DoubleRoom, DeluxeRoom
from RoomVisitor import RoomPriceVisitor, RoomMaintenanceVisitor, RoomReserveVisitor

class Client:

    single_room = SingleRoom()
    double_room = DoubleRoom()
    deluxe_room = DeluxeRoom()

    room_price_visitor = RoomPriceVisitor()
    single_room.accept(room_price_visitor)
    print("Single: ", single_room.room_price)

    room_maintenance_visitor = RoomMaintenanceVisitor()
    single_room.accept(room_maintenance_visitor)

    room_reserve_visitor = RoomReserveVisitor()
    single_room.accept(room_reserve_visitor)

    room_price_visitor = RoomPriceVisitor()
    double_room.accept(room_price_visitor)
    print("Double: ", double_room.room_price)


