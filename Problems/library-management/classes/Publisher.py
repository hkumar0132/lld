from classes.Member import Member


class Publisher(Member):
    def __init__(self, id, name):
        super().__init__(id, name)