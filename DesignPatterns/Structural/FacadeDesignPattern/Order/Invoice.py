from random import randint

class Invoice:
    def generate_invoice(self):
        print(f'Invoice number {randint(1, 100)}')