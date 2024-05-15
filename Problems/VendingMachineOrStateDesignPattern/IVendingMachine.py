from abc import ABC, abstractmethod
from typing import List

from Inventory import Inventory
from Coin import Coin

class IVendingMachine(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_coins(self) -> List[Coin]:
        pass
    
    @abstractmethod
    def set_coins(self):
        pass

    @abstractmethod
    def set_inventory(self):
        pass
    
    @abstractmethod
    def get_inventory(self) -> Inventory:
        pass

    @abstractmethod
    def set_vending_machine_state(self):
        pass

    @abstractmethod
    def get_vending_machine_state(self):
        pass
