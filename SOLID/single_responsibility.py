'''
    A class should have only one reason to change
'''

'''
    Class below has 3 reasons to change -> change
    in logic for saving to DB, saving to disk and console
    printing.
    This is violating the single responsibility principle
'''

class Invoice:

    def save_to_db(self):
        pass

    def save_to_disk(self):
        pass

    def save_to_console(self):
        pass


'''
    Now there are different classes having one reason
    to change each
'''

class InvoiceDB:
    def save_to_db(self):
        pass

class InvoiceDisk:
    def save_to_disk(self):
        pass

class InvoiceConsole:
    def save_to_console(self):
        pass