from .Book import Book

class User:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name
        self.borrowed_books : list[Book] = []

    def add_borrowed_book(self, book: Book):
        self.borrowed_books.append(book)

    def remove_borrowed_book(self, book: Book):
        for curr_book in self.borrowed_books:
            if curr_book['book'].id == book.id:
                self.borrowed_books.remove(curr_book)
                break

    def get_borrowed_books(self):
        return self.borrowed_books