from models.Expense import Expense


class EqualExpense(Expense):
    def __init__(self, paid_by, amount, split_into):
        self.paid_by = paid_by
        self.amount = amount
        self.split_into = split_into
    
    def get_paid_by(self):
        return self.paid_by
    
    def get_amount(self):
        return self.amount
    
    def get_split_into(self):
        return self.split_into