from abc import ABC, abstractmethod

class IInternalButton(ABC):

    @abstractmethod
    def press_button():
        pass
