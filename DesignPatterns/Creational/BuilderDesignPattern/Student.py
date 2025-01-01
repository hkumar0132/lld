
from IStudentBuilder import IStudentBuilder


class Student:

    def __init__(self, builder: IStudentBuilder) -> None:
        self.roll_no = getattr(builder, "roll_no", "NA")
        self.name = getattr(builder, "name", "NA")
        self.age = getattr(builder, "age", "NA")
        self.standard = getattr(builder, "standard", "NA")
        self.subjects = getattr(builder, "subjects", [])

    def to_string(self):
        return f'Roll No: {self.roll_no}\nName: {self.name}\nAge: {self.age}\nStandard: {self.standard}'
