class Account:
    def __init__(account_number, amount):
        pass

    def debit(amount):
        pass

    def credit(amount):
        pass

class Notes(Enum):
    HUNDRED=100
    FIVE_HUNDRED=500
    THOUSAND=1000

class CashDispenser:
    def __init__(self, denominations: List[Notes]):
        self.denominations = dict() # { HUNDRED: 10, FIVE_HUNDRED: 500, ... }


    def get_denominations_against_amount(self, amount, denominations=dict()):
        
        if amount > Notes.THOUSAND:
            required = amount // Notes.THOUSAND
            current = self.denominations[Notes.THOUSAND]
            amount -= min(current, required) * Notes.THOUSAND
            denominations[Notes.THOUSAND] = min(current, required)
        
        if amount > Notes.FIVE_HUNDRED:
            required = amount // Notes.FIVE_HUNDRED
            current = self.denominations[Notes.FIVE_HUNDRED]
            amount -= min(current, required) * Notes.FIVE_HUNDRED
            denominations[Notes.FIVE_HUNDRED] = min(current, required)

        if amount > Notes.HUNDRED:
            required = amount // Notes.HUNDRED
            current = self.denominations[Notes.HUNDRED]
            amount -= min(current, required) * Notes.HUNDRED
            denominations[Notes.HUNDRED] = min(current, required)

        return denominations, (amount == 0)
        
    def can_process_amount(self, amount):
        if amount < Notes.HUNDRED:
            raise Exception("Minimum 100")
        _, possible = self.get_denominations_against_amount(amount)
        return possible

    def withdraw_cash(self, amount):
        denominations, _ = self.get_denominations_against_amount(amount)
        for denomination in denominations.keys():
            self.denominations[denomination] -= denominations[denomination]
        return denominations

    def add_cash(denomination: Notes):
        pass

class Card:
    def __init__(self, number: str, pin: str, account: Account) -> None:    
        self.pin = pin
        self.account = account

    def update_pin(self):
        pass

    def get_pin(self):
        return self.pin
    
    def get_account(self):
        return self.account

from abc import ABC, abstractmethod
import uuid
class Transaction(ABC):
    def __init__(self, amount, account):
        self.id = uuid.uuid4()
        self.amount = amount
        self.account = account

    @abstractmethod
    def execute(self):
        pass

class DepositTransaction(Transaction):
    def __init__(self, amount, account: Account):
        super().__init__(amount, account)

    def execute(self):
        self.account.credit(self.amount)

class WithdrawalTransaction(Transaction):
    def __init__(self, amount, account: Account):
        super().__init__(amount, account)

    def execute(self, amount):
        if amount > self.amount:
            raise Exception("Insufficient funds")
        self.account.debit(self.amount)

class BankingService:
    def __init__(self):
        self.transactions = dict() # transaction_id -> Transaction

    def get_balance(account):
        return account.get_balance()

    def process_transaction(transaction: Transaction):
        transaction.execute()

    def debit(self, amount, account):
        transaction = WithdrawalTransaction(amount, account)
        self.transactions[transaction.id] = transaction
        self.process_transaction(transaction)

from threading import Lock
class ATMService:
    def __init__(self, banking_service: BankingService,  cash_dispenser: CashDispenser) -> None:
        self.banking_service = banking_service
        self.cards = dict() # card number -> Card
        self.cash_dispenser = cash_dispenser
        self.lock = Lock()

    def add_card(self, card):
        self.cards[card.get_number()] = card

    def __authenticate_card(self, card_number, pin):
        card = self.cards[card_number]
        if not card or card.pin != pin:
            raise Exception("Not valid")
        return card

    def get_balance(self, card_number, pin):
        card = self.__authenticate_card(card_number, pin)
        return self.banking_service.get_balance(card.get_account())

    def withdraw_cash(self, card_number, pin, amount):
        card = self.__authenticate_card(card_number, pin)
        with self.lock:
            if not self.cash_dispenser.can_process_amount(amount):
                print("Insufficient funds")
                return False
            
            self.banking_service.debit(amount, card.get_account())
            self.cash_dispenser.withdraw_cash(amount)

    def deposit_cash(self, notes: List[Note]):
        with self.lock:
            pass

