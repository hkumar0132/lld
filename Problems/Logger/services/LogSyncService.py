from collections import defaultdict
from .LoggingService import LoggingService
from .UserManagementService import UserManagementService

from enums.LogSyncType import LogSyncType

class LogSyncService:
    def __init__(self, logging_service: LoggingService, user_service: UserManagementService) -> None:
        self.log_syncs = defaultdict()
        self.logging_service = logging_service
        self.user_service = user_service

    def start_log_sync(self, log_ids, log_sync_type: LogSyncType):
        pass

    def get_log_sync_status(self, log_sync_id):
        pass

    def cancel_log_sync(self, log_sync_id):
        pass