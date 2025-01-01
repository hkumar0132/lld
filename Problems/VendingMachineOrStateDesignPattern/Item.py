class Item:
    def __init__(self, product_code: str, price: int) -> None:
        self.product_code = product_code
        self.price = price

    def get_price(self):
        return self.price
    
    def get_product_code(self):
        return self.product_code