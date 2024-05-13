from LRUEvictionPolicy import LRUEvictionPolicy
from DictBasedStorage import DictBasedStorage


class LRUCache:
    def __init__(self):
        self.storage = DictBasedStorage()
        self.eviction_policy = LRUEvictionPolicy()
        
    def put_item(self, key, value):
        put_success = self.storage.put(key, value)
        
        # STORAGE IS FULL
        if not put_success:
            key_at_head = self.eviction_policy.remove_most_recent_used()
            self.remove_item(key_at_head)
            self.storage.put(key, value)
        self.eviction_policy.key_accessed(key)
    
    def get_item(self, key):
        result = self.storage.get(key)
        if result:
            self.eviction_policy.key_accessed(key)
            return result
    
    def remove_item(self, key):
        self.storage.remove(key)
        self.eviction_policy.evict_key(key)