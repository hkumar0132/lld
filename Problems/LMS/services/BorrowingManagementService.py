from classes.Book import Book
from .LibraryManagementService import LibraryManagementService
from .UserManagementService import UserManagementService
from constants import MAXIMUM_BORROWING_ALLOWED

class BorrowingManagementService:
    def __init__(self, lms: LibraryManagementService, ums: UserManagementService) -> None:
        self.lms = lms
        self.ums = ums

    def borrow_book(self, user_id: str, book_id: str, due_date: str):
        user = self.ums.get_user_by_id(user_id)
        if not user:
            raise Exception(f"User with ID {user_id} not found.")
        
        book = self.lms.search_by_book_id(book_id)
        if not book or len(book) == 0:
            raise Exception(f"Book with ID {book_id} not found in the library.")
        
        if len(user.borrowed_books) >= MAXIMUM_BORROWING_ALLOWED:
            raise Exception("User has reached the maximum limit of borrowed books.")
        
        self.lms.remove_book(book[0])
        user.add_borrowed_book({
            'book': book[0],
            'due_date': due_date
        })
        print(f"Book '{book[0].title}' borrowed by {user.name}.")

    def return_book(self, user_id: str, book_id: str):
        user = self.ums.get_user_by_id(user_id)
        if not user:
            raise Exception(f"User with ID {user_id} not found.")
        
        books = self.ums.get_all_books_by_user_id(user_id)
        books_borrowed = False
        for book in books:
            if book.id == book_id:
                books_borrowed = True
                self.lms.add_book(book)
                user.remove_borrowed_book(book)
                print(f"Book '{book.title}' returned by {user.name}.")
                break

        if not books_borrowed:
            raise Exception(f"User has not borrowed the book with ID {book_id}.")