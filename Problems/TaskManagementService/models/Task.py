from Enums.Priority import Priority
from Enums.TaskStatus import TaskStatus
from .User import User

class Task:
    def __init__(self, id, name, priority: Priority, user: User, title, description, due_date) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.name = name
        self.priority = priority
        self.user = user
        self.date = due_date
        self.status = TaskStatus.PENDING

    def set_task_name(self, name: str):
        pass

    def set_task_email(self, email: str):
        pass

    def set_task_user(self, user: User):
        pass

    def set_status(self, status: TaskStatus):
        self.status = status