from Observer.Alert import Alert

class SMSAlert(Alert):
    def __init__(self, iphoneObservable):
        self.stock = iphoneObservable
        
    def update(self):
        # print(f'SMSALERT self.stock.get_stock_count(): {self.stock.get_stock_count()}')
        if self.stock.get_stock_count() != 0:
            print('updated observer SMS alert')