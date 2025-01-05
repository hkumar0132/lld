from .BookShelf import BookShelf
from .Book import Book

class Library:
    def __init__(self, id: str) -> None:
        self.id = id
        self.book_shelves : list[BookShelf] = []
    
    def add_shelf(self, shelf: BookShelf):
        self.book_shelves.append(shelf)

    def add_book(self, book: Book):
        for shelf in self.book_shelves:
            books = shelf.get_all_books()
            book_copy_found = False
            for curr_book in books:
                if book.title == curr_book:
                    book_copy_found = True
                    break
                
            if not book_copy_found:
                shelf.add_book(book)
                break

    def remove_book(self, book):
        for shelf in self.book_shelves:
            shelf.remove_book(book)

    def search_by_book_id(self, id):
        for shelf in self.book_shelves:
            books = shelf.get_all_books()
            for curr_book in books:
                if curr_book.id == id:
                    return [curr_book]
        return []

    def search_by_title(self, title):
        books = []
        for shelf in self.book_shelves:
            curr_books = shelf.get_all_books()
            for curr_book in curr_books:
                if curr_book.title == title:
                    books.append(curr_book)
        return books
                
    def search_by_author(self, author):
        books = []
        for shelf in self.book_shelves:
            curr_books = shelf.get_all_books()
            for curr_book in curr_books:
                if curr_book.author == author:
                    books.append(curr_book)
        return books
                
    def search_by_publisher(self, publisher):
        books = []
        for shelf in self.book_shelves:
            curr_books = shelf.get_all_books()
            for curr_book in curr_books:
                if curr_book.publisher == publisher:
                    books.append(curr_book)
        return books