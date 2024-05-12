from Order import Product, Payment, Invoice, Alert

class OrderFacade:
    def __init__(self):
        self.product : Product = Product()
        self.payment : Payment = Payment()
        self.invoice : Invoice = Invoice()
        self.alert : Alert = Alert()

    def create_order(self):
        print(self.product.get_product(2))
        self.payment.make_payment()
        self.invoice.generate_invoice()
        self.alert.send_notification()

        print("ORDER CREATED")