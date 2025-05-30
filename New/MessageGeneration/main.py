'''
Requirements:
1. Different customer types
2. Different message types
3. Different message for each customer type
4. Easy to add customer type/message type without much modification

'''

Core Entities:
1. Message
    - PrimePromoMessage
    - GuestPromoMessage
2. Customer
    - Prime
    - Guest
3. MessageType (Enum)
4. CustomerType (Enum)

Design:

enums/
from enum import Enum
class CustomerType(Enum):
    PRIME='PRIME'
    GUEST='GUEST'

class MessageType(Enum):
    PROMO='PROMO'
    DELIVERY_UPDATE='DELIVERY_UPDATE'

from abc import ABC, abstractmethod
class Message(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_message(self):
        pass

class PrimePromoMessage(Message):
    def create_message(self, customer: Customer):
        return f"Hi, {customer['name']}, enjoy prime benefits"

class GuestPromoMessage(Message):
    def create_message(self, customer: Customer):
        return f"Hi, {customer['name']}, signup to prime for full access: https://primevideo/subscription"
    
class Customer:
    def __init__(self, customer_id: str, name: str, email: str, customer_type: CustomerType):
        self.customer_id

class MessageFactory:
    def get_message_strategy(self, message_type: MessageType, customer_type: CustomerType):
        if message_type == MessageType.PROMO:
            if customer_type == CustomerType.PRIME:
                return PrimePromoMessage()
            elif customer_type == CustomerType.GUEST:
                return GuestPromoMessage()
            else:
                raise Exception("customer type does not exist")
        else:
            raise Exception('Message type does not exists')
        
class MessageService:
    def __init__(self, message_factory: MessageFactory):
        self.message_factory = message_factory

    def generate_message(self, message_type: MessageType, customer: Customer):
        message_strategy = self.message_factory.get_message_strategy(message_type, customer.customer_type)
        return message_strategy.create_message(customer)
    
import uuid    
def main():
    message_factory = MessageFactory()
    message_service = MessageService(message_factory)

    customer = Customer(
        uuid.uuid4(),
        'Himanshu',
        '',
        CustomerType.PRIME
    )
    message = message_service.generate_message(MessageType.PROMO, customer)
    print(message)

main()


