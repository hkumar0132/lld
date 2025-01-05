from services.UserManagementService import UserManagementService
from services.LibraryManagementService import LibraryManagementService
from services.BorrowingManagementService import BorrowingManagementService

def main():
    ums = UserManagementService([
        { 'name': 'Himanshu'},
        { 'name': 'A' },
        { 'name': 'B' },
        { 'name': 'C' },
        { 'name': 'D' }
    ])
    lms = LibraryManagementService()
    bms = BorrowingManagementService(lms, ums)

    borrowed = ums.get_all_books_by_user_id(1)
    print("BORROWED: ", borrowed)

    bms.borrow_book(1, 1, '2024-02-05')
    borrowed = ums.get_all_books_by_user_id(1)

    print("BORROWED: ")
    for book in borrowed:
        print("ID: ", book.id)

    bms.return_book(1, 1)
    borrowed = ums.get_all_books_by_user_id(1)

    print("BORROWED: ")
    for book in borrowed:
        print("ID: ", book.id)

    search_by_id = lms.search_by_book_id(1)
    print("search_by_id: ")
    for a in search_by_id:
        print(a.title)

    search_by_title = lms.search_by_title('The Alchemist')
    print("search_by_title: ")
    for a in search_by_title:
        print(a.title)

    search_by_author = lms.search_by_author('RXYZ')
    print("search_by_author: ")
    for a in search_by_author:
        print(a.title)

    search_by_publisher = lms.search_by_publisher('publisher 3')
    print("search_by_publisher: ")
    for a in search_by_publisher:
        print(a.title)

if __name__ == "__main__":
    main()