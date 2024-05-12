from Book import Book
from BookIterator import BookIterator
from Library import Library

class Client:

    books = [
        Book("HC Verma"),
        Book("Principles of Management"),
        Book("Thoughtful investor")
    ]

    lib = Library(books)
    itr = lib.create_iterator()

    while itr.has_next():
        print(itr.next())