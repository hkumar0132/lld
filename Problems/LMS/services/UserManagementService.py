from classes.User import User
from classes.Book import Book

class UserManagementService:

    def __init__(self, user_details) -> None:
        self.users : list[User] = []
        self.__create_users(user_details)

    def __create_users(self, user_details):
        for idx in range(len(user_details)):
            self.users.append(User(idx + 1, user_details[idx]['name']))

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user

    def get_all_books_by_user_id(self, user_id: str) -> list[Book]:
        books_borrowed = []
        for user in self.users:
            if user.id == user_id:
                for book in user.get_borrowed_books():
                    books_borrowed.append(book['book'])
        return books_borrowed