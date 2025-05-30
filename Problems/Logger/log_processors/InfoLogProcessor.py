from enums.LogLevel import LogLevel
from ..models.LogProcessor import LogProcessor

from models.Log import Log

class InfoLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: LogProcessor) -> None:
        super().__init__(LogLevel.INFO, next_log_processor)

    def process(self, log_level, log: Log):
        if log_level == LogLevel.INFO:
            print('')
        else:
            self.next_log_processor.process(log_level, log)