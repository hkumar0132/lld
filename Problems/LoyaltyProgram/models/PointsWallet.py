class PointsWallet:
    def __init__(self, point_wallet_id, points, user_id) -> None:
        self.point_wallet_id = point_wallet_id
        self.points = points
        self.user_id = user_id

    def add_points(self, points):
        self.points += points

    def substract_points(self, points):
        self.points -= points