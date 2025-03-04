from .Transaction import Transaction

class RedemptionTransaction(Transaction):

    def __init__(self, transaction_id, points_wallet_id, transaction_type, created_at, redemption_points, amount_gained) -> None:
        super().__init__(transaction_id, points_wallet_id, transaction_type, created_at)
        self.redemption_points = redemption_points
        self.amount_gained = amount_gained