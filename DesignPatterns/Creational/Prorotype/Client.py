from Student import Student

class Client:

    student = Student("Himanshu", 23, 21)
    student_clone = student.clone()

    print(type(student))
    print(type(student_clone))