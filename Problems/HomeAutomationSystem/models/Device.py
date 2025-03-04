from abc import ABC, abstractmethod
class Device(ABC):
    def __init__(self, device_id) -> None:
        self.device_id = device_id

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
