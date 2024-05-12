from typing import List

from IStudentBuilder import IStudentBuilder
from Student import Student

class StudentBuilder(IStudentBuilder):
    def __init__(self) -> None:
        self.subjects: List[str] = []

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self
    
    def set_standard(self, standard):
        self.standard = standard
        return self

    def build(self) -> Student:
        # Passing object of StudentBuilder to Student class
        return Student(self)