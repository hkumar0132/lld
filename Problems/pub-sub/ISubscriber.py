from models.Subscriber import Subscriber


class ISubscriber(Subscriber):
    def __init__(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
      
    def update(self, message):
        print(f'{self.id} received {message}')
        
        