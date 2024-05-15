from typing import List

from State import State
from IVendingMachine import IVendingMachine
from Coin import Coin

class Idle(State):

    def press_insert_coin_button(self, vending_machine: IVendingMachine):
        print("Insert coin button")
        vending_machine.set_coins([])
        vending_machine.set_vending_machine_state(HasMoney())

class HasMoney(State):

    def insert_coin(self, vending_machine: IVendingMachine, coins: List[Coin]):
        print("Insert coin")
        vending_machine.set_coins(coins)

    def start_product_selection(self, vending_machine: IVendingMachine):
        print("Start product selection")
        vending_machine.set_vending_machine_state(SelectProduct())

    def cancel_and_refund_money(self, vending_machine: IVendingMachine):
        print("Cancel and refund full money")
        vending_machine.set_vending_machine_state(Idle())

class SelectProduct(State):
    def select_product(self, vending_machine: IVendingMachine, product_code: str):

        item = vending_machine.get_inventory().get_item_with_product_code(product_code)
        coins = vending_machine.get_coins()

        total_amount = 0
        for coin in coins:
            total_amount += coin.get_value()
        if item.get_price() > total_amount:
            print(f"Insufficient fund: short by {item.get_price() - total_amount} cents")
            self.cancel_and_refund_money(vending_machine)
            return
        elif item.get_price() <= total_amount:
            self.refund_change_if_applicable(total_amount - item.get_price())
            vending_machine.set_vending_machine_state(DispenseProduct())

    def cancel_and_refund_money(self, vending_machine: IVendingMachine):
        print("Cancel and refund full money")
        vending_machine.set_vending_machine_state(Idle())

    def refund_change_if_applicable(self, change):
        if (change > 0):
            print(f"Refunding change in dispense tray {change}")

class DispenseProduct:
    def __init__(self) -> None:
        print("Product dispensed in tray")