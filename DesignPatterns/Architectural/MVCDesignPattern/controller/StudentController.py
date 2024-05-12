from model import Student
from view import StudentView

class StudentController:

    def __init__(self, model: Student, view: StudentView) -> None:
        self.model = model
        self.view = view

    def get_student_name(self):
        return self.model.get_name()
    
    def get_student_roll_no(self):
        return self.model.get_roll_no()
    
    def set_student_name(self, name: str):
        self.model.set_name(name)

    def set_student_roll_no(self, roll_no: str):
        self.model.set_roll_no(roll_no)

    def update_view(self):
        self.view.update(self.model.get_name(), self.model.get_roll_no())

