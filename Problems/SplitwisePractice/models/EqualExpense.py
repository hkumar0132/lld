from .Expense import Expense
class EqualExpense(Expense):
    def __init__(self, expense_id, group_id, created_by_user_id, expense_type, split_into_user_ids, split_amount) -> None:
        self.split_amount = split_amount
        super().__init__(expense_id, group_id, created_by_user_id, expense_type, split_into_user_ids)