from abc import ABC, abstractclassmethod

class Topic(ABC):
    @abstractclassmethod
    def add_subscriber(self):
        pass
    
    @abstractclassmethod
    def remove_subscriber(self):
        pass
    
    @abstractclassmethod
    def _notify_subscribers(self):
        pass
    
    @abstractclassmethod
    def publish_message(self):
        pass
    
    @abstractclassmethod
    def remove_message(self):
        pass