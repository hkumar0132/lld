from .Device import Device
from threading import Lock

class Thermostat(Device):
    def __init__(self, device_id, temperature) -> None:
        super().__init__(device_id)
        self.is_on = False
        self.temperature = temperature
        self.lock = Lock()

    def turn_on(self):
        with self.lock:
            self.is_on = True

    def turn_off(self):
        with self.lock:
            self.is_on = False
    
    def set_temperature(self, temperature):
        self.temperature = temperature
