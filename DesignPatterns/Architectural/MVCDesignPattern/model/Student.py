class Student:

    def __init__(self) -> None:
        self.name = ''
        self.roll_no = ''

    def get_roll_no(self):
        return self.roll_no
    
    def get_name(self):
        return self.name
    
    def set_roll_no(self, roll_no):
        self.roll_no = roll_no
    
    def set_name(self, name):
        self.name = name