from Director import Director
from EngineeringStudentBuilder import EngineeringStudentBuilder
from MBAStudentBuilder import MBAStudentBuilder

class Client:

    engineer = Director(EngineeringStudentBuilder())
    mba = Director(MBAStudentBuilder())

    student1 = engineer.create_student()
    student2 = mba.create_student()

    print(student1.to_string())
    print(student2.to_string())