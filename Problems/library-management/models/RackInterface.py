from abc import ABC, abstractclassmethod

class RackInterface:
    def __init__(self):
        pass
        
    @abstractclassmethod
    def get_id(self):
        pass
    
    @abstractclassmethod
    def add_book_to_rack(self):
        pass
    
    @abstractclassmethod
    def get_books_in_rack(self):
        pass
    
    @abstractclassmethod
    def _check_if_book_copy_exist(self):
        pass
    