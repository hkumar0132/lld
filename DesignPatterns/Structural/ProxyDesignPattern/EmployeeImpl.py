from Employee import Employee

class EmployeeImpl(Employee):
    def create(self):
        print("Employee created")

    def get(self):
        print("Returning employee")

    def delete(self):
        print("Employee deleted")