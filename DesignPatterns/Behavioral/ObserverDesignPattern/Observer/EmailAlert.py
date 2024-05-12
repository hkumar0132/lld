from .Alert import Alert
from Observable import Stock

class EmailAlert(Alert):
    def __init__(self, observable: Stock):
        self.observable = observable

    def __send_message_on_email(self):
        print("Message sent")
        
    def update(self):
        self.__send_message_on_email()