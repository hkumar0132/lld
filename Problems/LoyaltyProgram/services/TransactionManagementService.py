from .UserManagementService import UserManagementService
from .PointsWalletService import PointsWalletService

class TransactionManagementService:

    def __init__(self, user_service: UserManagementService, points_service: PointsWalletService) -> None:
        self.transactions = []
        self.user_service = user_service
        self.points_service = points_service

    def create_point_transaction(self, amount_spent, user_id):
        pass

    def redeemp_points(self, points, user_id):
        pass
