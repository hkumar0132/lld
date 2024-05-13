from Library import Library
from classes.Book import Book


def main():
    i = None
    library = None
    while True:
        if i == 'exit':
            break
        
        i = input()
        i = i.split(' ')
        if i[0] == 'create_library':
            library_id = i[1]
            no_of_racks = i[2]
            library = Library(library_id, int(no_of_racks))
            print(f'Created library with {no_of_racks} racks')
        elif library:
            if i[0] == 'add_book':
                book_id = i[1]
                title = i[2]
                comma_separated_authors = i[3]
                comma_separated_publishers = i[4]
                comma_separated_book_copy_ids = i[5]
                library.add_book(book_id, title=title, comma_separated_authors=comma_separated_authors, comma_separated_publishers=comma_separated_publishers, comma_separated_book_copy_ids=comma_separated_book_copy_ids)
            elif i[0] == 'remove_book_copy':
                book_copy_id = i[1]
                library.remove_book_copy(book_copy_id)
            elif i[0] == 'borrow_book':
                book_id = i[1]
                user_id = i[2]
                due_date = i[3]
                library.borrow_book(book_id, user_id, due_date)
            elif i[0] == 'borrow_book_copy':
                book_copy_id = i[1]   
                library.borrow_book_copy(book_copy_id) 
            elif i[0] == 'return_book_copy':
                book_copy_id = i[1]
                library.return_book_copy(book_copy_id)
            elif i[0] == 'search':
                attribute = i[1]
                attribute_value = i[2]
                if attribute == 'book_id':
                    library.search_book_id(attribute_value)
                elif attribute == 'author_id':
                    library.search_author(attribute_value)
                elif attribute == 'publisher_id':
                    library.search_publisher(attribute_value)
                else:
                    print('\nInvalid Input')
            elif i[0] == 'print_borrowed':
                library.print_borrowed(i[1])
            else:
                print('\nInvalid Input')
        else:
            print('\nInvalid Input')
            
            
    
if __name__ == "__main__":
    main()
