from abc import ABC, abstractmethod

from IVendingMachine import IVendingMachine

class State(ABC):

    def press_insert_coin_button(self, vending_machine: IVendingMachine):
        raise Exception("Operation not allowed")
    
    def insert_coin(self, vending_machine: IVendingMachine):
        raise Exception("Operation not allowed")
    
    def start_product_selection(self, vending_machine: IVendingMachine):
        raise Exception("Operation not allowed")

    def select_product(self, vending_machine: IVendingMachine):
        raise Exception("Operation not allowed")
    
    def cancel_and_refund_money(self, vending_machine: IVendingMachine):
        raise Exception("Operation not allowed")
    
    def dispense_product_button(self, vending_machine: IVendingMachine):
        raise Exception("Operation not allowed")
    
    def refund_change_if_applicable(self, vending_machine: IVendingMachine):
        raise Exception("Operation not allowed")