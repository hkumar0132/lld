from models.Storage import Storage


class DictBasedStorage(Storage):
    def __init__(self):
        self.capacity = 5
        self.keys = dict()
        
    def get(self, key):
        return self.keys[key] if key in self.keys else None
    
    def put(self, key, value):
        if len(self.keys) < self.capacity or key in self.keys:
            self.keys[key] = value
            return True
        return False
    
    def remove(self, key):
        if key in self.keys:
            self.keys.pop(key)
    