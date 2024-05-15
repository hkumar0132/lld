from typing import List

from ItemShelf import ItemShelf
from Item import Item

class Inventory:
    def __init__(self, item_shelves: List[ItemShelf]) -> None:
        self.item_shelves = item_shelves

    def get_item_with_product_code(self, product_code: str) -> Item:
        for item_shelf in self.item_shelves:
            items = item_shelf.get_items()
            for item in items:
                if item.get_product_code() == product_code:
                    return item