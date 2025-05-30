from .Device import Device
from threading import Lock

class Light(Device):
    def __init__(self, device_id, brightness) -> None:
        super().__init__(device_id)
        self.is_on = False
        self.brightness = brightness
        self.lock = Lock()

    def turn_on(self):
        with self.lock:
            self.is_on = True

    def turn_off(self):
        with self.lock:
            self.is_on = False
    
    def set_brightness(self, brightness):
        self.brightness = brightness
