from Employee import Employee
from EmployeeImpl import EmployeeImpl

class EmployeeProxy(Employee):

    def __init__(self) -> None:
        self.employee_impl = EmployeeImpl()

    def create(self, role):
        if (role == "ADMIN"):
            self.employee_impl.create()
            return
        raise Exception("Access denied")

    def get(self, role):
        if (role == "ADMIN" or role == "USER"):
            self.employee_impl.get()
            return
        raise Exception("Access denied")

    def delete(self, role):
        if (role == "ADMIN"):
            self.employee_impl.delete()
            return
        raise Exception("Access denied")