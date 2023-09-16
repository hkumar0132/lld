from Observer.Alert import Alert

class EmailAlert(Alert):
    def __init__(self, iphoneObservable):
        self.stock = iphoneObservable
        
    def update(self):
        if self.stock.get_stock_count() != 0:
            print('updated observer email alert')