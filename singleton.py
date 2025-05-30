from threading import Lock

class CoffeeMachine:
    _instance = None
    _lock = Lock()

    def __init__(self) -> None:
        if CoffeeMachine._instance is not None:
            # Instantiating class even when one instance has already been created
            raise Exception("")
        CoffeeMachine._instance = self

    @classmethod(function)
    def __new__(cls):
        with cls.lock:
            if cls._instance is None:
                CoffeeMachine()
            return cls._instance