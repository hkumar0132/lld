from .Book import Book

class Rack:
    def __init__(self, number) -> None:
        self.number = number
        self.books : list[Book] = []

    def get_all_books(self) -> list[Book]:
        return self.books
    
    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)