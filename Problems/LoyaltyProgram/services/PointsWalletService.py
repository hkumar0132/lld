class PointsWalletService:

    def __init__(self, user_service) -> None:
        self.points_wallets = []
        self.user_service = user_service

    def update_point_wallet(self, user_id, points, type='subtract'):
        pass
