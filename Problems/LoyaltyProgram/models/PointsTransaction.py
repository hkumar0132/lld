from .Transaction import Transaction

class PointsTransaction(Transaction):

    def __init__(self, transaction_id, points_wallet_id, transaction_type, created_at, amount_spent, points_gained) -> None:
        super().__init__(transaction_id, points_wallet_id, transaction_type, created_at)
        self.amount_spent = amount_spent
        self.points_gained = points_gained