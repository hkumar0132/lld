from classes.Member import Member


class Author(Member):
    def __init__(self, id, name):
        super().__init__(id, name)