from StudentBuilder import StudentBuilder

class MBAStudentBuilder(StudentBuilder):
    def set_subjects(self):
        self.subjects = ["A", "B", "C"]
        return self