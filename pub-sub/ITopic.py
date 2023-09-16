
from models.Topic import Topic
from threading import Thread


class ITopic(Topic):
    def __init__(self):
        self.subscribers = set()
        self.messages = []
        
    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)
    
    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)
    
    def _notify_subscribers(self, message):
        def notify(subscriber):
            subscriber.update(message)
            
        threads = []
        
        # Create and start thread
        for subscriber in self.subscribers:
            thread = Thread(target=notify, args=(subscriber,))
            threads.append(thread)
            thread.start()
            
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
    
    def publish_message(self, message):
        self.messages.append(message)
        self._notify_subscribers(message.get_message())
    
    def remove_message(self, message):
        self.messages.remove(message)