class RetryManager:
    def __init__(self, retry_id, email_message_id, retry_count, max_retry, retry_technique='backoff') -> None:
        self.retry_id = retry_id
        self.email_message_id = email_message_id
        self.retry_count = retry_count
        self.max_retry = max_retry
        self.retry_technique = retry_technique

    def set_retry_count(self, retry_count):
        self.retry_count = retry_count