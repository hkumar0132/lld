from IMessage import IMessage
from IPublisher import IPublisher
from ISubscriber import ISubscriber
from ITopic import ITopic
from models.Queue import Queue


class IQueue(Queue):
    def __init__(self):
        self.topics = set()
        self.subscribers = set()
        self.publishers = set()
        
    def add_new_topic(self):
        topic = ITopic()
        self.topics.add(topic)
        return topic
    
    def get_new_subscriber(self):
        new_subscriber = ISubscriber(len(self.subscribers))
        self.subscribers.add(new_subscriber)
        return new_subscriber
    
    def get_new_publisher(self):
        new_publisher = IPublisher(len(self.publishers))
        self.publishers.add(new_publisher)
        return new_publisher
    
    def add_new_subscriber_to_topic(self, topic, subscriber):
        if topic in self.topics:
            topic.add_subscriber(subscriber)
        else:
            raise BaseException('Topic does not exist')
            
    def publish_message(self, publisher, topic, message):
        if publisher in self.publishers and topic in self.topics:
            publisher.publish(topic, message)
        else:
            raise BaseException('Publisher or topic does not exist')
            
    def create_new_message(self, message):
        return IMessage(message)
    
    def remove_topic(self, topic):
        self.topics.remove(topic)
    
    def get_topics(self):
        return self.topics