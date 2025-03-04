from .Metric import Metric

class GroupMetric(Metric):
    def __init__(self, metric_id, metric_type, total_balance, total_expense, group_id, top_debtor_id, top_owed_id) -> None:
        super().__init__(metric_id, metric_type, total_balance, total_expense)
        self.group_id = group_id
        self.top_debtor_id = top_debtor_id
        self.top_owed_id = top_owed_id