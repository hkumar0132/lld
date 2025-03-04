from enums.NotificationStatus import NotificationStatus

class Notification:
    def __init__(self, notification_id, message, user_ids, status=NotificationStatus.PENDING) -> None:
        self.notification_id = notification_id
        self.message = message
        self.user_ids = user_ids
        self.status = status

    def set_status(self, status):
        self.status = status