'''
    A class should be open for extension but closed for modification
'''

'''
    Below class is open for modification
    as anyone can add new methods in this class: 
    save_to_disk, save_to_mongodb and this makes it prone to 
    bugs in production as save_to_db was already live
'''

class Invoice:
    def save_to_db(self):
        pass

class Invoice:
    def save_to_db(self):
        pass

    def save_to_disk(self):
        pass

    def save_to_mongodb(self):
        pass

'''
    We should create interface to solve this
'''

from abc import ABC, abstractmethod
class InvoiceI(ABC):
    @abstractmethod
    def save():
        pass

class InvoiceDB(InvoiceI):
    def save():
        print("Save to DB")

'''
    I can add new method by creating another class and implementing
    the interface InvoiceI
'''

class InvoiceDisk(InvoiceI):
    def save():
        print("Save to disk")

class InvoiceMongoDB(InvoiceI):
    def save():
        print("Save to MongoDB")