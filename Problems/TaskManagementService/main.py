from services.UserManagementService import UserManagementService
from services.TaskManagementService import TaskManagementService
from Enums.Priority import Priority

def main():
    ums = UserManagementService()
    tms = TaskManagementService()

    user = ums.create_user()

    tms.append_task(1, "Do Laundry", Priority.LOW)
    tms.fetch_tasks()

if __name__ == "__main__":
    main()