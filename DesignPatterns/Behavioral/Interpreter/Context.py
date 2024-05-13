class Context:

    def __init__(self) -> None:
        self.map : dict[str, int] = {}

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        if key in self.map:
            return self.map[key]