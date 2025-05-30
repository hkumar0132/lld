'''
Requirements:
1. The online shopping service should allow users to add them to the shopping cart, and place orders.
2. The system should support multiple product categories
3. The system should handle inventory management and update product availability accordingly.
4. The system should handle concurrent user requests and ensure data consistency.
'''

Core Entities:
    
1. Order
2. Cart
3. User
4. Product
5. CartItem
6. OrderStatus

Design:
    
enums/
from enums import Enum
class OrderStatus(Enum):
    PENDING='PENDING'
    CONFIRMED='CONFIRMED'
    DELIVERED='DELIVERED'
    SHIPPED='SHIPPED'
    CANCELLED='CANCELLED'
    
models/

from abc import ABC, abstractmethod
class Discount(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    def apply_discount(self):
        pass

import math
class FixedDiscount(Discount):
    def __init__(self, name: str, description: str, discount_amount: int):
        super.__init__(name, description)
        self.discount_amount = discount_amount
    
    def apply_discount(self, amount: int):
        return math.max(amount - self.discount_amount, 0)

class PercentageDiscount(Discount):
    def __init__(self, name: str, description: str, percentage: int):
        super.__init__(name, description)
        if percentage < 0 or percentage > 100:
            raise Exception("Percentage invalid")
        self.percentage = percentage
    
    def apply_discount(self, amount: int):
        return math.max(amount - amount * percentage * 0.01, 0)
    
class BuyTwoGetOneFree(Discount):
    def __init__(self, name: str, description: str, eligible_product_id: str):
        super.__init__(name, description)
        self.eligible_product_id = eligible_product_id

    def apply_discount(self, amount: int, items: List[Item]):
        for item in items:
            if item.id == self.eligible_product_id:
                discount = (item.product.quantity * item.product.price) // 3
                return math.max(amount - discount, 0)

class CouponFilter(ABC):
    @abstractmethod
    def is_coupon_applicable(self, product: Product):
        pass
    
class ProductCategoryFilter(CouponFilter):
    def __init__(self, products: List[Product]):
        self.products = products
    
    def is_coupon_applicable(self, product: Product):
        return len(p for for p in self.products if p == product) > 0

class ProductIdFilter(CouponFilter):
    def __init__(self, products: List[str]):
        self.product_ids = product_ids
    
    def is_coupon_applicable(self, product: Product):
        return len(p for for p in self.products if p.id == product.id) > 0
        
from datetime import datetime        
class Coupon:
    def __init__(self, discount: Discount, filter: CouponFilter, expiry_time: datetime):
        self.discount = discount
        self.filter = filter
        self.expiry_time = expiry_time

    def is_valid(self):
        return self.expiry_time <= datetime.now()

    def is_coupon_applicable(self, product):
        return self.filter.is_coupon_applicable(product)
        
    def apply(self, amount: int):
        return self.discount.apply_discount(amount)
        
from abc import ABC, abstractmethod
class Payment:
    @abstractmethod
    def process_payment(self, amount: int):
        pass

class UPIPayment(Payment):
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        pass    
    
class Order:
    def __init__(self, user: User, items: List[Item], address: Address, price: int, status: OrderStatus="PENDING"):
        self.user = user
        self.items = items
        self.status = status
        self.address = address
        self.price = price
    
    def update_status(self, new_status: OrderStatus):
        self.status = new_status

class Cart:
    def __init__(self, user: User, items: List[Items]=[],
        cart_level_discounts: List[Discount]=[]):
        self.user = user
        self.items = items
        self.cart_level_discounts = cart_level_discounts
        self.coupons = []
        
    def add_coupon(self, coupon: Coupon):
        applicable = False
        for item in self.items:
            if coupon.is_coupon_applicable(item.product):
                applicable = True
                break
        
        if applicable:
            self.coupons.append(coupon)
            return True
        return False
    
    def add_item(self, item: Item):
        self.items.append(item)

    def delete_item(self, item_to_delete: Item):
        self.items = [item for item in self.items if item_to_delete != item ]
    
    def clear_cart(self):
        self.items = []
        
    def get_items(self) -> List[Item]:
        return self.items
        
    def get_total_after_item_level_discounts(self):
        return sum(item.get_discounted_price() for item in self.items)
        
    def __apply_cart_level_discounts(self, total_price: int):
        for discount in self.cart_level_discounts:
            total_price = discount.apply_discount(total_price)
        return max(total_price, 0)
        
    def __apply_coupons(self, total_price: int):
        for coupon in self.coupons:
            if not coupon.is_valid():
                raise Exception('Coupon not valid')
            total_price = coupon.apply(total_price)
        return max(total_price, 0)
        
    def get_total(self):
        return sum(item.quantity * item.product.get_price() for item in self.items)
    
    def get_subtotal(self):
        total_price = self.get_total_after_item_level_discounts()
        total_price = self.__apply_cart_level_discounts(total_price)
        total_price = self.__apply_coupons(total_price)
        return total_price
        
    
class Address:
    def __init__(self, lat: str, long: str, city: str, pincode: str):
        self.lat = lat
        self.long = long
        self.city = city
        self.pincode = pincode
    
from typing import List    
class User:
    def __init__(self, name: str, email: str, orders: List[Order], addresses: List[Address]):
        self.name = name
        self.email = email
        self.orders = orders
        self.addresses = addresses
    
from threading import Lock   
import uuid
class Product:
    def __init__(self, name: str, title: str, category: str, price: int, quantity:int=0):
        self.id = uuid.uuid4()
        self.name = name
        self.title = title
        self.category = category
        self.quantity = quantity
        self.price = price
        self.reserved = 0
        self.lock = Lock()
        
    def update_quantity(self, quantity):
        with self.lock:
            self.quantity += quantity
    
    def reserve_product(self, quantity: int):
        with self.lock:
            if quantity > self.quantity - self.reserved:
                raise Exception('Cannot be greater than available')
        
            self.reserved += quantity
            
    def unreserve_product(self, quantity: int):
        with self.lock:
            if quantity > self.reserved:
                raise Exception('cannot be greater than available')
                
            self.reserved -= quantity

    def get_price(self):
        return self.price

    def update_price(self, new_price: int):
        with self.lock:
            self.price = new_price

class Item:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.discounts = []
        
    def add_discount(self, discount: Discount):
        self.discounts.append(discount)
        
    def add_quantity(self, quantity: int):
        self.quantity += quantity
        
    def remove_quantity(self, quantity: int):
        if quantity > self.quantity:
            raise Exception("Insufficient quantity")
        self.quantity -= quantity
        
    def get_discounted_price(self):
        total_price = self.product * self.quantity
        for discount in self.discounts:
            total_price = discount.apply(self.product * self.quantity)
        return total_price
        
services/

class PaymentService:
    def __init__(self, pay_strategy: Payment) -> None:
        self.pay_strategy = pay_strategy
    
    def process_payment(self, amount):
        self.pay_strategy.process_payment(amount)

from threading import Lock
class CartService:
    def __init__(self):
        self.carts = []
    
    def create_cart(self, user: User):
        cart = Cart(
            user
        )
        self.carts.append(cart)
        return cart
    
    def add_product(self, cart: Cart, product: Product, quantity: int):
        if not product.reserve_product(quantity):
            raise Exception("Unable to reserve product")
        items = cart.get_items()
        for item in items:
            if item.product.id == product.id:
                item.add_quantity(quantity)
                return
        cart.add_item(Item(product, quantity))
            
    def remove_product(self, cart: Cart, product: Product, quantity: int):
        items = cart.get_items()
        for item in items:
            if item.product.id == product.id:
                item.remove_quantity(quantity)
                with self.lock:
                    product.unreserve_product(quantity)

    def delete_product(self, cart: Cart, item: Item):
        cart.delete_item(item)
        item.product.unreserve_product(item.quantity)

    def clear_cart(self, cart: Cart):
        for c in self.carts:
            if c == cart:
                cart.clear_cart()
                items = cart.get_items()
                for item in items:
                    item.product.unreserve_product(item.quantity)

class OrderService:

    def __init__(self, cart_service: CartService, payment_service: PaymentService):
        self.cart_service = cart_service
        self.payment_service = payment_service
        self.orders = []
        
    def create_order(self, user: User, cart: Cart, address: Address):
        
        items = cart.get_items()
        total_price = cart.get_subtotal()
        
        order = Order(
            user,
            items,
            address,
            total_price,
            status=OrderStatus.PENDING,
        )

        self.orders.append(order)
        return order
    
    def confirm_order(self, order: Order):
        try:

            self.payment_service.process_payment(order.price)
            
            order.update_status(
                OrderStatus.CONFIRMED
            )
        
            for item in order.items:
                item.product.update_quantity(-item.quantity)
                item.product.unreserve_product(item.quantity)
        except Exception as e:

            

exceptions/


controllers/
def main():
    pass

main()    