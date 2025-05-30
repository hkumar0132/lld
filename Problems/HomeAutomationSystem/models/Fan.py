from threading import Lock
from .Device import Device

class Fan(Device):
    def __init__(self, device_id, speed) -> None:
        super().__init__(device_id)
        self.is_on = False
        self.speed = speed
        self.lock = Lock()

    def turn_on(self):
        with self.lock:
            self.is_on = True

    def turn_off(self):
        with self.lock:
            self.is_on = False
    
    def set_speed(self, speed):
        self.speed = speed
