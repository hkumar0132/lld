class Transaction:

    def __init__(self, transaction_id, points_wallet_id, transaction_type, created_at) -> None:
        self.transaction_id = transaction_id
        self.points_wallet_id = points_wallet_id
        self.transaction_type = transaction_type
        self.created_at = created_at