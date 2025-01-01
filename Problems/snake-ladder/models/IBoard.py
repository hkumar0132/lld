from abc import ABC, abstractmethod

class IBoard(ABC):

    @abstractmethod
    def initialize_board():
        pass

    @abstractmethod
    def get_object_at_cell():
        pass