import uuid

from enums.LogLevel import LogLevel
from ..models.LogProcessor import LogProcessor

class CriticalLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: LogProcessor) -> None:
        super().__init__(LogLevel.CRITICAL, next_log_processor)

    def process(self, log_level, data):
        if log_level == LogLevel.CRITICAL:
            print('')
        else:
            self.next_log_processor.process(log_level, data)