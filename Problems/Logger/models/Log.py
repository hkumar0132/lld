import uuid

class Log:
    def __init__(self, log_level, created_at, log_data, log_type) -> None:
        self.log_id = uuid.uuid4()
        self.log_level = log_level
        self.created_at = created_at
        self.log_data = log_data
        self.log_type = log_type