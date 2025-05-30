'''
Design Vending machine

Requirements:

1. Allow product selection, coins and dispensing product
2. Handle change refunds
3. Handle insufficient balance scenarios
4. Inventory management
5. Allow cancellation

'''

Core Entities:
    
1. Coin
2. Product
3. Inventory
4. VendingMachineState
    - IdleState
    - ProductSelectionState
    - DispenseState
    - RefundState
- State design pattern

Design:

from enum import Enum    
class Coin(Enum):
    ONE=1
    TWO=2
    FIVE=5
    TEN=10

class Product:
    def __init__(self, name: str, item_code: str, price: int):
        self.name = name
        self.item_code = item_code
        self.price = price
        
from collections import defaultdict
from threading import Lock
class Inventory:
    def __init__(self):
        self.inventory = defaultdict(int) # item_code -> { total, reserved }
        self.lock = Lock()
    
    def add_product(self, product: Product, quantity: int, reserved: int):
        self.inventory[product.item_code] += quantity
        
    def get_product_quantity(self, product: Product):
        total, reserved = self.inventory[product.item_code][]
        return total - reserved

    def decrease_quantity(self, product, quantity: int):
        with self.lock:
            if product.item_code not in self.inventory:
                raise Exception('Cannot decrease quantity - product does not exist')
            if quantity > self.get_product_quantity(product):
                raise Exception('Insufficient quantity')
            self.inventory[product.item_code] -= quantity
            if self.inventory[product.item_code] == 0:
                del self.inventory[product.item_code]

from abc import ABC, abstractmethod        
class VendingMachineState(ABC):        
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine
    
    @abstractmethod
    def insert_coin(self, coin: Coin):
        pass
    
    @abstractmethod
    def select_product(self, product: Product):
        pass
    
    @abstractmethod
    def dispense_product(self, product: Product):
        pass
    
    @abstractmethod
    def return_change(self):
        pass
    
    @abstractmethod
    def cancel(self):
        pass
    
class IdleState(VendingMachineState):
    def __init__(self, vending_machine: VendingMachine):
        super().__init__(vending_machine)        
    
    def insert_coin(self, coin: Coin):
        self.vending_machine.add_coin(coin)
        self.vending_machine.set_state(self.vending_machine.product_selectio_state)
        
    def select_product(self, product: Product):
        raise Exception("please insert coin first")
    
    def dispense_product(self, product: Product):
        raise Exception("please insert coin first")
    
    def return_change(self):
        raise Exception("please insert coin first")
    
    def cancel(self):
        raise Exception("Machine already in idle state")

class ProductSelectionState(VendingMachineState):
    def __init__(self, vending_machine: VendingMachine):
        super().__init__(vending_machine)        
    
    def insert_coin(self):
        raise Exception("cannot insert coin now")
    
    def select_product(self, product: Product, quantity: int):
        if self.vending_machine.inventory.get_product_quantity(product) <= quantity:
            self.vending_machine.product_selected = product
            self.vending_machine.product_quantity = quantity
            self.vending_machine.set_state(self.vending_machine.dispense_state)
            print("Product selected")
        else:
            print("Insufficient quantity")
            self.vending_machine.set_state(self.vending_machine.idle_state)
        
    def dispense_product(self, product: Product):
        raise Exception("please select product first")
    
    def return_change(self):
        raise Exception("please select product first")
        
    def cancel(self):
        print("Transaction cancelled")
        print(f"Refunding money: {self.vending_machine.amount_paid}")
        self.vending_machine.reset_payment()
        self.vending_machine.set_state(self.vending_machine.idle_state)
       
 class DispenseState(VendingMachineState):
    def __init__(self, vending_machine: VendingMachine):
        super().__init__(vending_machine)        
    
    def insert_coin(self):
        raise Exception("cannot insert coin now")
    
    def select_product(self, product: Product):
        raise Exception("cannot select product now")
    
    def dispense_product(self, product: Product, quantity: int):
        self.vending_machine.inventory.decrease_quantity(product, quantity)
        print("Product dispensed")
        self.vending_machine.set_state(self.vending_machine.refund_state)

    def return_change(self):
        raise Exception('Not allowed')
        
    def cancel(self):
        print("Transaction cancelled")
        print(f"Refunding {self.vending_machine.amount_paid}")
        self.vending_machine.reset_product_selected()
        self.vending_machine.reset_payment()
        self.vending_machine.set_state(self.vending_machine.idle_state)

class ReturnChangeState(VendingMachineState):
    def __init__(self, vending_machine: VendingMachine):
        super().__init__(vending_machine)        
    
    def insert_coin(self):
        raise Exception("cannot insert coin now")
    
    def select_product(self, product: Product):
        raise Exception("already selected")
    
    def dispense_product(self, product: Product):
        raise Exception("already dispensed")
    
    def return_change(self):
        change = self.vending_machine.amount_paid - self.vending_machine.product_selected.price * self.vending_machine.product_quantity
        if change > 0:
            self.vending_machine.reset_payment()
            print(f"Change dispensed {change}")
        else:
            print("No change to return")

        self.vending_machine.reset_product_selected()
        self.vending_machine.set_state(self.vending_machine.idle_state)

from typing import List    
class VendingMachine:
    def __init__(self, inventory: Inventory, products: List[Product]):
        self.state = IdleState()
        self.amount_paid = 0
        self.inventory = inventory # code -> quantity
        self.products = products
        self.product_selected = None
        self.product_quantity = 0
        
        self.idle_state = IdleState(self)
        self.product_selection_state = ProductSelectionState(self)
        self.dispense_state = DispenseState(self)
        self.refund_state = ReturnChangeState(self)
        
        self.state = self.idle_state
    
    def set_state(self, state: VendingMachineState):
        self.state = state
        
    def add_coin(self, coin: Coin):
        self.amount_paid += coin.value
        
    def insert_coin(self, coin: Coin):
        self.state.insert_coin(coin)
    
    def select_product(self, product: Product, quantity: int):
        self.state.select_product(product, quantity)

    def dispense_product(self):
        self.state.dispense_product(self.product_selected, self.product_quantity)
        
    def return_change(self):
        self.vending_machine.return_change()
        
    def cancel(self):
        self.state.cancel()
        
    def reset_product_selected(self):
        self.inventory.add_product(self.product_selected, self.product_quantity)
        self.product_quantity = 0
        self.product_selected = None

    def reset_payment(self):
        self.amount_paid = 0

class Transaction:
    user_to_product_selection = dict() # user_id -> { product_selected, quantity }