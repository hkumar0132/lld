from typing import List
from Book import Book

from Iterator import Iterator

class BookIterator(Iterator):

    def __init__(self, books: List[Book]) -> None:
        self.books = books
        self.index = 0

    def next(self):
        if self.has_next():
            self.index += 1
            return self.books[self.index - 1].book_name
        return None

    def has_next(self):
        return self.index < len(self.books)