class DuplicateException(Exception):
    def __init__(self, message="Duplicate Exception"):
        super().__init__(message)