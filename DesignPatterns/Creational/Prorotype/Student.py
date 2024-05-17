from IPrototype import IPrototype

class Student(IPrototype):

    def __init__(self, name, age, roll_no) -> None:
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def clone(self) -> IPrototype:
        return Student(self.name, self.age, self.roll_no)