class LogSizeLimitException(Exception):
    def __init__(self, message='Log too large') -> None:
        super().__init__(message)