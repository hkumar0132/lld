from .Room import Room
from .Enums.DeviceActions import DeviceActions

class SmartHome:
    def __init__(self) -> None:
        self.rooms : list[Room] = []

    def add_room(self, room: Room):
        self.room.append(room)

    def remove_room(self, room_id):
        self.room = [room for room in self.room if room.room_id != room_id]

    def add_device(room_id, device_id):
        pass

    def remove_device(room_id, device_id):
        pass

    def control_all_device(self, room_id, action=DeviceActions):
        pass

    def control_device_by_id(self, room_id, device_id, action=DeviceActions):
        pass