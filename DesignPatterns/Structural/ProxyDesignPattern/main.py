from EmployeeProxy import EmployeeProxy

def main():

    try:
        employee = EmployeeProxy()
        employee.create("ADMIN")
        employee.get("USER")
        employee.create("USER")
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()