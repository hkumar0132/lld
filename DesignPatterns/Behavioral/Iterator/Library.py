from typing import List

from Book import Book
from Aggregator import Aggregator
from BookIterator import BookIterator

class Library(Aggregator):

    def __init__(self, books: List[Book]) -> None:
        self.books = books

    def create_iterator(self):
        return BookIterator(self.books)
