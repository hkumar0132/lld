import uuid

from enums.LogLevel import LogLevel
from ..models.LogProcessor import LogProcessor

class ErrorLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: LogProcessor) -> None:
        super().__init__(LogLevel.ERROR, next_log_processor)

    def process(self, log_level, data):
        if log_level == LogLevel.ERROR:
            print('')
        else:
            self.next_log_processor.process(log_level, data)