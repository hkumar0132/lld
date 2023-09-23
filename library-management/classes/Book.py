class Book:
    def __init__(self, id, title, list_of_authors, list_of_publishers) -> None:
        self.id = id
        self.title = title
        self.list_of_authors = list_of_authors
        self.list_of_publishers = list_of_publishers
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_list_of_authors(self):
        return self.list_of_authors
    
    def get_list_of_publishers(self):
        return self.list_of_publishers