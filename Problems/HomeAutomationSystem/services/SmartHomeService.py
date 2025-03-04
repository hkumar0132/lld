from ..models.Enums.DeviceActions import DeviceActions

class SmartHomeService:
    def __init__(self, smart_home, user_service) -> None:
        self.smart_home = smart_home
        self.user_service = user_service

    def add_room(self, room_id):
        pass

    def remove_room(self, room_id):
        pass

    def add_device(room_id, device_id):
        pass

    def remove_device(room_id, device_id):
        pass

    def control_all_device(self, user_id, room_id, action=DeviceActions):
        pass

    def control_device_by_id(self, user_id, room_id, device_id, action=DeviceActions):
        pass