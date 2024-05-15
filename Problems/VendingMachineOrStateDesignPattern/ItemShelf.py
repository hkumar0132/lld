from typing import List
from Item import Item

class ItemShelf:
    def __init__(self, shelf_no, items) -> None:
        self.shelf_no = shelf_no
        self.items: List[Item] = items

    def get_items(self):
        return self.items