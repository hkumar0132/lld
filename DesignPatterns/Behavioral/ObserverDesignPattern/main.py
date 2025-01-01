from Observable import IphoneStock, Stock
from Observer import EmailAlert, NotificationAlert, SmsAlert

def main():
    iphoneObservable: Stock = IphoneStock()
    
    email = EmailAlert(iphoneObservable)
    sms = SmsAlert(iphoneObservable)
    notification = NotificationAlert(iphoneObservable)
    
    iphoneObservable.add(email)
    iphoneObservable.add(sms)
    iphoneObservable.add(notification)
    
    iphoneObservable.set_stock_count(1)
    iphoneObservable.set_stock_count(2)

if __name__ == "__main__":
    main()