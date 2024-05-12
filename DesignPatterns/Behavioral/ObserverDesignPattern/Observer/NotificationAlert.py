from .Alert import Alert
from Observable import Stock

class NotificationAlert(Alert):
    def __init__(self, observable: Stock):
        self.observable = observable

    def __send_app_notification(self):
        print("Notification sent")
        
    def update(self):
        self.__send_app_notification()