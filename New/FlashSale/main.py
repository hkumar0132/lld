class Product:
    def __init__(self, product_id: str, name: str, title: str):
        pass

class SaleItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.reserved = 0

from datetime import datetime, timedelta
from threading import Lock
from collections import OrderedDict, defaultdict

class FlashSale:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.sale_items = dict() # product_id -> SaleItem
        self.start_time = start_time
        self.end_time = end_time
        self.product_locks = Lock()

        self.reservation_timestamp = defaultdict(OrderedDict()) # product_id -> { user_id1: {start_time, quantity}, user_id2: {} }

        self.timeout = timedelta(minutes=15)

    def add_item(self, sale_item: SaleItem):
        self.sale_items[sale_item.product.product_id] = sale_item

    def get_product(self, product: Product):
        return self.sale_items[product.product_id]
    
    def is_sale_valid(self):
        curr_time = datetime.now()
        return curr_time<= self.end_time and curr_time >= self.start_time    
    
    # O(1)
    def get_available_quantity(self, product: Product):
        return self.sale_items[product.product_id].quantity - self.sale_items[product.product_id].reserved
    
    def release(self, key1, key2):
        del self.reservation_timestamp[key1][key2]

    def is_expired(self, timestamp1, timestamp2):
        return timestamp1 - timestamp2 > self.timeout
    
    def __release_expired_reservations(self, product_id):

        # Loop through the ordered list to delete the oldest reservations
        for user_id, value in self.reservation_timestamp[product_id].items():
            start_time, _ = value
            if self.is_expired(datetime.now(), start_time):
                self.reservation_timestamp[product_id].pop(user_id)
            else:
                break

    # Efficient -> Only deleting from begining
    def try_reserve(self, user: User, product: Product, quantity: int):
        with self.product_locks[product.product_id]:
            self.__release_expired_reservations()
            if quantity > self.get_available_quantity(product):
                return False
            self.reservation_timestamp[product.product_id][user.user_id] = (datetime.now(), quantity)
            # reserving quantity
            self.sale_items[product.product_id].reserved += quantity
            return True
        
    # O(1)
    def confirm_reservation(self, user: User, product: Product, quantity: int):
        with self.product_locks[product.product_id]:
            start_time, quantity = self.reservation_timestamp[product.product_id][user.user_id]
            if datetime.now() - start_time > self.timeout:
                self.sale_items[product.product_id].reserved -= quantity
                self.release(product.product_id, user.user_id)
                print("Reservation already expired")
                return False
            
            self.sale_items[product.product_id].quantity -= quantity
            self.sale_items[product.product_id].reserved -= quantity
            self.release((user.user_id, product.product_id))
            return True

class OrderStatus(Enum):
    PENDING='PENDING'
    CONFIRMED='CONIFRMED'
    CANCELLED='CANCELLED'

class OrderItem:
    product    
    quantity

class Order:
    def __init__(self, order_id: str, order_items: OrderItem, order_status: OrderStatus='PENDING'):
        self.order_id = order_id
        self.order_status = order_status
        self.order_items = order_items

    def update_status(self, status: OrderStatus):
        self.order_status = status

    def get_order_items(self):
        return self.order_items

class OrderService:

    def __init__(self, flash_sale: FlashSale):
        self.flash_sale = flash_sale
        self.orders = dict()

    def create_purchase(self, product: Product, quantity: int):
        if not self.flash_sale.is_sale_valid():
            raise Exception("Sale not valid")

        item = self.flash_sale.get_product(product)

        if not item:
            raise Exception("Item not part of sale")
        
        if self.flash_sale.try_reserve(product, quantity):
            order_id = uuid.uuid4()
            order = Order(
                order_id,
                [
                    OrderItem(
                        product,
                        quantity
                    )
                ]
            )
            self.orders[order_id] = order

            return order_id
        
    def update_purchase():
        pass

    def confirm_order(self, order_id):
        if order_id not in self.orders:
            raise Exception("Invalid")

        order = self.orders[order_id]
        order_item = order.get_order_items()

        if self.flash_sale.confirm_reservation(order_item.product, order_item.quantity)
            order.update_status(OrderStatus.CONFIRMED)

def main():
    flash_sale = FlashSale()

    p1 = Product()
    p2 = Product()
    item1 = SaleItem(p1, 1000)
    item2 = SaleItem(p2, 20000)

    flash_sale.add_item(item1)

    order_service = OrderService(flash_sale)
    order_id = order_service.create_purchase(p1)
    if order_id:
        order_service.confirm_order(order_id)
    else:
        print("unable to reserve")

main()