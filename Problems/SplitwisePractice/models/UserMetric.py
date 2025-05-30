from .Metric import Metric

class UserMetric(Metric):
    def __init__(self, metric_id, metric_type, total_balance, total_expense, user_id) -> None:
        super().__init__(metric_id, metric_type, total_balance, total_expense)
        self.user_id = user_id