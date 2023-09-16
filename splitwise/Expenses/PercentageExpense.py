from models.Expense import Expense


class PercentageExpense(Expense):
    def __init__(self, paid_by, amount, split_into, split_into_percentage):
        self.paid_by = paid_by
        self.amount = amount
        self.split_into = split_into
        self.split_into_percentage = split_into_percentage
        
    def get_expense_type(self):
        return self.expense_type
    
    def get_paid_by(self):
        return self.paid_by
    
    def get_amount(self):
        return self.amount
    
    def get_split_into(self):
        return self.split_into
    
    def get_split_into_percentage(self):
        return self.split_into_percentage