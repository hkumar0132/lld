from models.RackInterface import RackInterface


class Rack(RackInterface):
    def __init__(self, rack_id):
        self.rack_id = rack_id
        self.book = None
        
    def get_id(self):
        return self.rack_id
    
    def add_book_to_rack(self, book_id, book_copy_id):
        if self.book != None:
            return
        self.book = { 'book_id': book_id, 'book_copy_id': book_copy_id }
    
    def get_book(self):
        return self.book
    
    def get_book_copies_by_book_id(self, book_id):
        if book_id in self.books:
            return self.books[book_id]
    
    def check_if_book_exist(self):
        return self.book

    def remove_book_copy(self):
        self.book = None
        
    