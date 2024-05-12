from model import Student
from view import StudentView
from controller import StudentController

def main():
    student_model = Student()
    student_view = StudentView()

    student_controller = StudentController(student_model, student_view)
    student_controller.update_view()

    student_controller.set_student_roll_no('24')
    student_controller.set_student_name('Himanshu')

    student_controller.update_view()

if __name__ == "__main__":
    main()