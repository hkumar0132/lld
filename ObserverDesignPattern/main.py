from Observable.IphoneStock import IphoneStock
from Observer.EmailAlert import EmailAlert
from Observer.NotificationAlert import NotificationAlert
from Observer.SMSAlert import SMSAlert


def main():
    iphoneObservable = IphoneStock()
    
    #Observers
    email = EmailAlert(iphoneObservable)
    sms = SMSAlert(iphoneObservable)
    notification = NotificationAlert(iphoneObservable)
    
    iphoneObservable.add(email)
    iphoneObservable.add(sms)
    iphoneObservable.add(notification)
    
    iphoneObservable.set_stock_count(1)
    iphoneObservable.set_stock_count(2)

if __name__ == "__main__":
    main()