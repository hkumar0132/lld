from Expenses.EqualExpense import EqualExpense
from Expenses.ExactExpense import ExactExpense
from Expenses.PercentageExpense import PercentageExpense
from models.ExpenseType import ExpenseType


class ExpenseFactory:
    def get_expense(self, type, *args):
        # print('ARGS: ', *args)
        if type == ExpenseType.EQUAL:
            return EqualExpense(*args)
        elif type == ExpenseType.EXACT:
            return ExactExpense(*args)
        elif type == ExpenseType.PERCENT:
            return PercentageExpense(*args)
        return None