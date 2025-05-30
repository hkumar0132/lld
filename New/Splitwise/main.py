class User:
    name
    email

class Split:
    paid_by: User
    amount: int

class SplitStrategy:
    split_into: List[User]

    def apply_split() -> List[Split]:
        pass

class EqualSplitStrategy(SplitStrategy):
    split_into

class ExactSplitStrategy(SplitStrategy):
    split_into
    split_division

class Expense:
    paid_by: User
    splits: List[Split]
    group

class Group:
    users: List[User]
    expenses: List[Expense]

class ExpenseManager:
    pass