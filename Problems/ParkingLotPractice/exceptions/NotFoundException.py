class NotFoundException(Exception):
    def __init__(self, message = "Not found") -> None:
        super().__init__(message)