class Expense:
    def __init__(self, expense_id, group_id, created_by_user_id, expense_type, split_into_user_ids, category) -> None:
        self.expense_id = expense_id
        self.group_id = group_id
        self.created_by_user_id = created_by_user_id
        self.expense_type = expense_type
        self.split_into_user_ids = split_into_user_ids
        self.category = category