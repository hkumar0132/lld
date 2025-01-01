from abc import ABC, abstractmethod

class IExternalButton(ABC):

    @abstractmethod
    def press_button():
        pass