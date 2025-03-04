class Notification:
    def __init__(self, notification_id, message, device_ids, created_at) -> None:
        self.notification_id = notification_id
        self.message = message
        self.device_ids = device_ids
        self.created_at = created_at