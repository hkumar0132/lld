from collections import defaultdict

from .LogParserService import LogParseService
from Problems.Logger.log_processors.InfoLogProcessor import InfoLogProcessor
from Problems.Logger.log_processors.DebugLogProcessor import DebugLogProcessor
from Problems.Logger.log_processors.WarningLogProcessor import WarningLogProcessor
from Problems.Logger.log_processors.ErrorLogProcessor import ErrorLogProcessor
from Problems.Logger.log_processors.CriticalLogProcessor import CriticalLogProcessor
from models.Log import Log

class LoggingService:

    _instance = None

    def __init__(self, log_parser_service: LogParseService) -> None:
        self.logs = defaultdict()
        self.log_parser_service = log_parser_service

        if not LoggingService._instance:
            self.log_processor = InfoLogProcessor(DebugLogProcessor(WarningLogProcessor(ErrorLogProcessor(CriticalLogProcessor(None)))))
            LoggingService._instance = self

    def create(self, log_level, log_details):
        # Validation ->  LogSizeLimitException("log data cannot exceed 5KB")

        log = Log(log_level, log_details)

        self.log_processor.create(log_level, log)

        pass

    def get_log_details_by_id(self, log_id):
        pass

    def remove_log_by_id(self, log_id):
        pass

    def filer_log(filters=[]): # filters -> log_level, after_timestamp, before_timestamp
        pass

    def filter_log_by_keyword(self, keyword):
        pass
