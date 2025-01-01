from abc import ABC, abstractclassmethod

class UserInterface(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def get_id(self):
        pass