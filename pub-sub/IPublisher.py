from models.Publisher import Publisher


class IPublisher(Publisher):
    def __init__(self, id):
        self.id = id
        
    def publish(self, topic, message):
        topic.publish_message(message)
        
        