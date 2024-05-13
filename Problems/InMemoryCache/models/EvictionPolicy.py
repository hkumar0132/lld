from abc import ABC, abstractclassmethod

class EvictionPolicy(ABC):
    @abstractclassmethod
    def key_accessed(self):
        pass
    
    @abstractclassmethod
    def evict_key(self):
        pass
    
    @abstractclassmethod
    def remove_most_recent_used(self):
        pass
    