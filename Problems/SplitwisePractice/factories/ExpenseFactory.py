from enums.ExpenseType import ExpenseType
from models.EqualExpense import EqualExpense
from models.ExactExpense import ExactExpense
from models.PercentageExpense import PercentageExpense

class ExpenseFactory:

    def get_expense(expense_id, group_id, created_by_user_id, expense_type: ExpenseType, split_into_user_ids):
        if expense_type == ExpenseType.EQUAL:
            return EqualExpense()
        elif expense_type == ExpenseType.EXACT:
            return ExactExpense()
        elif expense_type == ExpenseType.PERCENTAGE:
            return PercentageExpense()
