from IQueue import IQueue
from threading import Thread


def main():
    queue = IQueue()
    
    topic1 = queue.add_new_topic()
    topic2 = queue.add_new_topic()
    
    producer1 = queue.get_new_publisher()
    producer2 = queue.get_new_publisher()
    
    consumer1 = queue.get_new_subscriber()
    consumer2 = queue.get_new_subscriber()
    consumer3 = queue.get_new_subscriber()
    consumer4 = queue.get_new_subscriber()
    consumer5 = queue.get_new_subscriber()
    
    queue.add_new_subscriber_to_topic(topic1, consumer1)
    queue.add_new_subscriber_to_topic(topic1, consumer2)
    queue.add_new_subscriber_to_topic(topic1, consumer3)
    queue.add_new_subscriber_to_topic(topic1, consumer4)
    queue.add_new_subscriber_to_topic(topic1, consumer5)
    
    queue.add_new_subscriber_to_topic(topic2, consumer1)
    queue.add_new_subscriber_to_topic(topic2, consumer3)
    queue.add_new_subscriber_to_topic(topic2, consumer4)
    
    def _publish_message_to_topic_by_producer(producer, topic, message):
        queue.publish_message(producer, topic, message)
    
    messages = [
        [producer2, topic1, queue.create_new_message('Message 1')],
        [producer1, topic1, queue.create_new_message('Message 2')],
        [producer2, topic1, queue.create_new_message('Message 3')],
        [producer1, topic2, queue.create_new_message('Message 4')],
        [producer2, topic2, queue.create_new_message('Message 5')]
    ]
    
    threads = []
    for message in messages:
        thread = Thread(target=_publish_message_to_topic_by_producer, args=(message[0], message[1], message[2]))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
    
if __name__ == "__main__":
    main()