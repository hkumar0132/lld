from collections import defaultdict

class UserManagementService:

    def __init__(self) -> None:
        self.user_id = defaultdict()

    def create_user(self, user_details, password):
        pass

    def login_user(self, email, password):
        # Return JWT token
        pass

    def remove_user(self, user_id):
        pass

    def update_user(self, user_id, updated_user_details):
        pass