class InvalidMove(Exception):
    def __init__(self, message="Invalid move"):
        super().__init__(message)