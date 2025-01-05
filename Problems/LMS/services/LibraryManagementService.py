from classes.Library import Library
from classes.Book import Book
from classes.Rack import Rack
from classes.BookShelf import BookShelf

class LibraryManagementService:
    def __init__(self) -> None:
        self.library : Library = None
        self.users = []

        self.__create_libary()

    def __create_libary(self):
        book1 = Book(1, 'The Alchemist', 'Paulo Coehlo', 'publisher 1')
        book2 = Book(2, 'Siddhartha', 'Herman Hesse', 'publisher 2')
        book3 = Book(3, 'Life of Pi', 'ABC', 'publisher 1')
        book4 = Book(4, 'The monk who sold his ferrari', 'Robin Sharma', 'publisher 1')
        book5 = Book(5, 'DEF', 'XYZ', 'publisher 3')

        book_shelf1 = BookShelf()

        rack1 = Rack(1)
        rack1.add_book(book1)
        rack1.add_book(book2)

        rack2 = Rack(2)
        rack2.add_book(book3)
        rack2.add_book(book4)
        rack2.add_book(book5)

        book_shelf1.add_rack(rack1)
        book_shelf1.add_rack(rack2)

        self.library = Library(1)
        self.library.add_shelf(book_shelf1)

    def add_book(self, book):
        self.library.add_book(book)

    def remove_book(self, book):
        self.library.remove_book(book)

    def search_by_book_id(self, id) -> Book:
        return self.library.search_by_book_id(id)

    def search_by_title(self, title):
        return self.library.search_by_title(title)

    def search_by_author(self, author):
        return self.library.search_by_author(author)
    
    def search_by_publisher(self, publisher):
        return self.library.search_by_publisher(publisher)