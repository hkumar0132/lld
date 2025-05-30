class DuplicateException(Exception):
    def __init__(self, message = "Already exists") -> None:
        super().__init__(message)