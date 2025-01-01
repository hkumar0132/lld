from StudentBuilder import StudentBuilder

class EngineeringStudentBuilder(StudentBuilder):
    def set_subjects(self) -> StudentBuilder:
        self.subjects = ["D", "E", "F"]
        return self
