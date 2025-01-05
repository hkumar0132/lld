from .Rack import Rack
from .Book import Book

class BookShelf:
    def __init__(self) -> None:
        self.racks : list[Rack] = []

    def add_rack(self, rack: Rack):
        self.racks.append(rack)
        # print("ADDED RACK: ", self.racks)

    def get_all_books(self) -> list[Book]:
        books = []
        # print(self.racks)
        for racks in self.racks:
            for book in racks.get_all_books():
                books.append(book)
        return books

    def add_book(self, book: Book):
        for rack in self.racks:
            book_copy_found = False
            for curr_book in rack.get_all_books():
                if curr_book.id == book.id:
                    book_copy_found = True
                    break
            
            if not book_copy_found:
                rack.add_book(book)
                break

    def remove_book(self, book: Book):
        for rack in self.racks:
            for curr_book in rack.get_all_books():
                if curr_book.id == book.id:
                    rack.remove_book(book)
                    break