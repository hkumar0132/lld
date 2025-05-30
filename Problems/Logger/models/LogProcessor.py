class LogProcessor:
    def __init__(self, next_log_processor) -> None:
        self.next_log_processor = next_log_processor

    def process(self, log_level, data):
        if self.next_log_processor:
            print('')