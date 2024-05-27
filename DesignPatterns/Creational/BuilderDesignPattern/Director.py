from StudentBuilder import Student
from EngineeringStudentBuilder import EngineeringStudentBuilder
from StudentBuilder import StudentBuilder

class Director:

    def __init__(self, student_builder: StudentBuilder) -> None:
        self.student_builder = student_builder

    def create_student(self):
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            return self.__create_engineering_student()
        return self.__create_MBA_student()

    def __create_MBA_student(self) -> Student:
        return self.student_builder.set_roll_no(28).set_standard("9").set_subjects().build()

    def __create_engineering_student(self) -> Student:
        return self.student_builder.set_roll_no(1).set_name("Abc").set_age(29).set_standard("9").set_subjects().build()