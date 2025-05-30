import uuid

from enums.LogLevel import LogLevel
from ..models.LogProcessor import LogProcessor

class WarningLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: LogProcessor) -> None:
        super().__init__(LogLevel.WARNING, next_log_processor)

    def create(self, log_level, data):
        if log_level == LogLevel.WARNING:
            print('')
        else:
            self.next_log_processor.create(log_level, data)