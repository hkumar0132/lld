from .Alert import Alert
from Observable import Stock

class SmsAlert(Alert):
    def __init__(self, observable: Stock):
        self.observable = observable

    def __send_message_on_mobile(self):
        print("Sms sent")
        
    def update(self):
        self.__send_message_on_mobile()