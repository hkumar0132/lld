class InvalidMoveExceptin(Exception):
    def __init__(self, message='Invalid move') -> None:
        super().__init__(message)