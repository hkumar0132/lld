from abc import ABC, abstractmethod

class IDisplay(ABC):

    @abstractmethod
    def get_floor_no():
        pass

    @abstractmethod
    def get_internal_button():
        pass

    @abstractmethod
    def set_floor_no():
        pass

    @abstractmethod
    def set_internal_button():
        pass