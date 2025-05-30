from .Expense import Expense

class PercentageExpense(Expense):
    def __init__(self, expense_id, group_id, created_by_user_id, expense_type, split_into_user_ids, split_into_amount, split_into_percentage) -> None:
        self.split_into_amount = split_into_amount
        self.split_into_percentage = split_into_percentage
        super().__init__(expense_id, group_id, created_by_user_id, expense_type, split_into_user_ids)