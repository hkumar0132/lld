from Users.NormalUser import NormalUser
from classes.Book import Book
from classes.Rack import Rack


class Library:
    def __init__(self, library_id, no_of_racks):
        self.library_id = library_id
        self.no_of_racks = no_of_racks
        self.list_of_racks = []
        
        # add book_id_to_book_copies_mapping
        
        self.id_to_book_mapping = {} # replace with book_id_to_book_mapping
        self.user_id_to_book_mapping = {} # replace with user_id_to_book_id_mapping
        
        self.author_to_book_mapping = {} # author to book_id mapping
        self.publisher_to_book_mapping = {} # publisher to book_id_mapping
        
        self.create_racks()
        
    def create_racks(self):
        for i in range(self.no_of_racks):
            rack = Rack(i+1)
            self.list_of_racks.append(rack)
            
    def add_book(self, book_id, title, comma_separated_authors, comma_separated_publishers, comma_separated_book_copy_ids):
        authors = comma_separated_authors.split(',')
        publishers = comma_separated_publishers.split(',')
        book_copy_ids = comma_separated_book_copy_ids.split(',')
        
        empty_racks = []
        for rack in self.list_of_racks:
            if not rack.check_if_book_exist():
                empty_racks.append(rack)
            if len(empty_racks) == len(book_copy_ids):
                break
        
        if len(empty_racks) >= len(book_copy_ids):        
            ''' 
                @TODO - instead of passing authors, publishers directly
                we should create their object
                and instead of using publisher_id directly, we should use publisher.get_id()
            '''
            book = Book(book_id, title, authors, publishers)
            if book_id not in self.id_to_book_mapping:
                self.id_to_book_mapping[book_id] = []
            self.id_to_book_mapping[book_id].append(book)
            for author in authors:
                if author not in self.author_to_book_mapping:
                    self.author_to_book_mapping[author] = []
                self.author_to_book_mapping[author].append(book)
                
            for publisher in publishers:
                if publisher not in self.publisher_to_book_mapping:
                    self.publisher_to_book_mapping[publisher] = []
                self.publisher_to_book_mapping[publisher].append(book)             
        
            print('\nAdded Book to racks: ') 
            for index, rack in enumerate(empty_racks):
                rack.add_book_to_rack(book_id, book_copy_ids[index])
                print(rack.get_id(),end=",")
        else:
            print('\nRack not available')
            
                
        print()
    def remove_book_copy(self, book_copy_id):
        for rack in self.list_of_racks:
            book = rack.get_book()
            if book and book['book_copy_id'] == book_copy_id:
                rack.remove_book_copy()
                print(f'Removed book copy: {book_copy_id} from rack: {rack.get_id()}')
    
    def borrow_book(self, book_id, user_id, due_date):
        user = NormalUser(len(self.user_id_to_book_mapping))
        if user.get_id() in self.user_id_to_book_mapping:
            if len(self.user_id_to_book_mapping[user.get_id()]) == 5:
                print('\nOverlimit')
                return
        if book_id not in self.id_to_book_mapping:
            print('\nInvalid Book ID')
            return
        for rack in self.list_of_racks:
            book = rack.get_book()
            if book and book["book_id"] == book_id:
                book_copy_id = book["book_copy_id"]
                if user_id not in self.user_id_to_book_mapping:
                    self.user_id_to_book_mapping[user_id] = []
                self.user_id_to_book_mapping[user_id].append({ 'book_id': book_id, 'book_copy_id': book_copy_id, 'due_date': due_date })
                rack.remove_book_copy()
                print(f'\nBorrowed Book from rack: {rack.get_id()}')
                return
            
        print('\nNot available')
        
    def borrow_book_copy(self, book_copy_id, user_id, due_date):
        user = NormalUser(len(self.user_id_to_book_mapping))
        if user.get_id() in self.user_id_to_book_mapping:
            if len(self.user_id_to_book_mapping[user.get_id()]) == 5:
                print('\nOverlimit')
                return
        
        for rack in self.list_of_racks:
            book = rack.get_book()
            if book and book["book_copy_id"] == book_copy_id:
                book_copy_id = book["book_copy_id"]
                if user_id not in self.user_id_to_book_mapping:
                    self.user_id_to_book_mapping[user_id] = []
                self.user_id_to_book_mapping[user_id].append({ 'book_id': '', 'book_copy_id': book_copy_id, 'due_date': due_date })
                rack.remove_book_copy()
                print(f'\nBorrowed Book from rack: {rack.get_id()}')
                return
        print('\nInvalid Book Copy ID')
                        
    def return_book_copy(self, book_copy_id):
        for user_id in self.user_id_to_book_mapping:
            for books in self.user_id_to_book_mapping[user_id]:
                if books['book_copy_id'] == book_copy_id:
                    book_id = books['book_id']
                    
                    for rack in self.list_of_racks:
                        if not rack.check_if_book_exist():
                            rack.add_book_to_rack(book_id, book_copy_id)
                            print(f'\nReturned book copy {book_copy_id} and added to rack: {rack.get_id()}')
                            return
            
    def print_borrowed(self, user_id):
        if user_id not in self.user_id_to_book_mapping or len(self.user_id_to_book_mapping[user_id]) == 0:
            return
        for book in self.user_id_to_book_mapping[user_id]:
            print(f'\nBook Copy: {book["book_copy_id"]} {book["due_date"]}')
            
    def search_book_id(self, book_id):
        if book_id not in self.id_to_book_mapping:
            return
        for book in self.id_to_book_mapping[book_id]:
            for rack in self.list_of_racks:
                b = rack.get_book()
                if b and b['book_id'] == book_id:
                    print(f'{b["book_copy_id"]} {book.get_id()} {book.get_title()} {book.get_list_of_authors()} {book.get_list_of_publishers()} {rack.get_id()} ',end="")
                    #{borrowed_by_id} {due_date}
                    for user_id in self.user_id_to_book_mapping:
                        if self.user_id_to_book_mapping[user_id]['book_id'] == book.get_id() and self.user_id_to_book_mapping[user_id]['book_copy_id'] == b.book_copy_id:
                            print(f'{user_id} {self.user_id_to_book_mapping[user_id]["due_date"]}')
                            break
                    print()
        
        # @TODO - print the borrowed books
        # for user_id in self.user_id_to_book_mapping:
        #     for book in self.user_id_to_book_mapping[user_id]:
        #         print(f'{book["book_copy_id"]} {book["book_id"]} {book.get_title()} {book.get_list_of_authors()} {book.get_list_of_publishers()} {rack.get_id()} ',end="")
        
    def search_publisher(self, publisher_id):
        if publisher_id not in self.publisher_to_book_mapping:
            print('\nNo books available')
            return
        print('\nBook Copy: ')
        for book in self.publisher_to_book_mapping[publisher_id]:
            for rack in self.list_of_racks:
                b = rack.get_book()
                if b and b['book_id'] == book.get_id():
                    print(f'{b["book_copy_id"]} {book.get_id()} {book.get_title()} {book.get_list_of_authors()} {book.get_list_of_publishers()} {rack.get_id()} ',end="")
                    #{borrowed_by_id} {due_date}
                    for user_id in self.user_id_to_book_mapping:
                        if self.user_id_to_book_mapping[user_id]['book_id'] == book.get_id() and self.user_id_to_book_mapping[user_id]['book_copy_id'] == b.book_copy_id:
                            print(f'{user_id} {self.user_id_to_book_mapping[user_id]["due_date"]}')
                            break
                    print()
            
    def search_author(self, author_id):
        if author_id not in self.author_to_book_mapping:
            print('\nNo books available')
            return
        print('\nBook Copy: ')
        for book in self.author_to_book_mapping[author_id]:
            for rack in self.list_of_racks:
                b = rack.get_book()
                if b and b['book_id'] == book.get_id():
                    print(f'{b["book_copy_id"]} {book.get_id()} {book.get_title()} {book.get_list_of_authors()} {book.get_list_of_publishers()} {rack.get_id()} ',end="")
                    #{borrowed_by_id} {due_date}
                    for user_id in self.user_id_to_book_mapping:
                        if self.user_id_to_book_mapping[user_id]['book_id'] == book.get_id() and self.user_id_to_book_mapping[user_id]['book_copy_id'] == b.book_copy_id:
                            print(f'{user_id} {self.user_id_to_book_mapping[user_id]["due_date"]}')
                            break
                    print()