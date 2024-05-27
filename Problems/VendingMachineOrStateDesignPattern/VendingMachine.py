from typing import List

from Coin import Coin
from Inventory import Inventory
from IVendingMachine import IVendingMachine
from State import State
from State.impl import Idle

class VendingMachine(IVendingMachine):

    def __init__(self) -> None:
        self.current_state = Idle()
        self.coins: List[Coin] = []

    def get_coins(self):
        return self.coins
    
    def set_coins(self, coins: List[Coin]):
        for coin in coins:
            self.coins.append(coin)

    def set_inventory(self, inventory: Inventory):
        self.inventory = inventory
    
    def get_inventory(self):
        return self.inventory

    def set_vending_machine_state(self, state: State):
        self.current_state = state

    def get_vending_machine_state(self):
        return self.current_state