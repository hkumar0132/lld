from abc import ABC, abstractclassmethod

class Queue(ABC):
    @abstractclassmethod
    def add_new_topic(self):
        pass
    
    @abstractclassmethod
    def remove_topic(self):
        pass
    
    @abstractclassmethod
    def get_new_subscriber(self):
        pass
    
    @abstractclassmethod
    def add_new_subscriber_to_topic(self):
        pass
    
    @abstractclassmethod
    def get_topics(self):
        pass