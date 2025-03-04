import uuid

class LogSync:
    def __init__(self, log_sync_type, log_ids) -> None:
        self.log_sync_id = uuid.uuid4()
        self.log_sync_type = log_sync_type
        self.log_ids = log_ids