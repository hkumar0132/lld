from abc import ABC, abstractmethod

class IPlayer(ABC):
    @abstractmethod
    def get_player_name(self):
        pass

    @abstractmethod
    def get_player_id(self):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def set_position(self):
        pass