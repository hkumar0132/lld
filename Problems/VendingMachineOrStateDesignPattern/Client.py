from VendingMachine import VendingMachine
from ItemShelf import ItemShelf
from Item import Item
from Inventory import Inventory
from Coin import Coin
from CoinType import CoinType

def fill_up_inventory(vending_machine: VendingMachine):
    item_shelves = []
    for i in range(3):
        items = []
        for j in range(3):
            price: int = 0
            if i == 0:
                price = 5
            elif j == 1:
                price = 15
            else:
                price = 24
            item = Item(f"0{i}{j}", price)
            items.append(item)
        
        item_shelf = ItemShelf(i, items)
        item_shelves.append(item_shelf)

    inventory = Inventory(item_shelves)
    vending_machine.set_inventory(inventory)
    

class Client:

    try:
        vending_machine = VendingMachine()
        fill_up_inventory(vending_machine)

        vending_machine_state = vending_machine.get_vending_machine_state()
        vending_machine_state.press_insert_coin_button(vending_machine)

        vending_machine_state = vending_machine.get_vending_machine_state()
        vending_machine_state.insert_coin(
            vending_machine,
            [
                Coin(CoinType.PENNY),
                Coin(CoinType.NICKEL),
                Coin(CoinType.PENNY),
                Coin(CoinType.QUARTER)
            ]
        )

        vending_machine_state.insert_coin(
            vending_machine,
            [
                Coin(CoinType.PENNY),
                Coin(CoinType.NICKEL),
                Coin(CoinType.PENNY),
                Coin(CoinType.NICKEL)
            ]
        )

        vending_machine_state = vending_machine.get_vending_machine_state()
        vending_machine_state.start_product_selection(vending_machine)

        vending_machine_state = vending_machine.get_vending_machine_state()
        vending_machine_state.select_product(vending_machine, "000")
    except Exception as err:
        print("error occured: ", err)