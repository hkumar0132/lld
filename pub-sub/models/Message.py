from abc import ABC, abstractclassmethod

class Message(ABC):
    @abstractclassmethod
    def get_message(self):
        pass