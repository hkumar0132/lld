from .UserManagementService import UserManagementService
from models.Task import Task
from Enums.Priority import Priority
from Enums.TaskStatus import TaskStatus
from exceptions.DuplicateException import DuplicateException
from collections import defaultdict

from threading import Lock

class TaskManagementService:
    def __init__(self, ums: UserManagementService) -> None:
        self.tasks = defaultdict(defaultdict(Task))

        for priority in Priority:
            self.tasks[priority] = dict()

        self.ums = ums
        self.lock = Lock()

    def search_task(self, keyword):
        # Search by title or description
        pass            

    def append_task(self, id, name, priority):

        with self.lock:
            for priority in sorted(Priority, key=lambda p: -p.value):
                task_id = self.tasks[priority][id]
                if task_id == id:
                    raise DuplicateException("Task with id already exists")

            task = Task(id, name, priority)
            self.ums.add_task_for_user(task)
            self.tasks[priority][id] = task
            
    def fetch_tasks(self, limit : int = 10):

        tasksWithPriority = []
        for priority in sorted(Priority, key=lambda p: -p.value):
            tasksWithPriority.extend(self.tasks[priority].values())
            if (len(tasksWithPriority) > limit):
                return tasksWithPriority[:limit]

        return tasksWithPriority[:limit]

    def remove_task_by_id(self):    
        with self.lock:
            pass

    def get_task_by_id(self):
        with self.lock:
            pass

    def complete_task(self, task_id):
        with self.lock:
            for priority in sorted(Priority, key=lambda p: -p.value):
                task = self.tasks[priority][task_id]
                if task:
                    task.set_status(TaskStatus.COMPLETED)                    

    def get_next_task(self):
        for priority in sorted(Priority, key=lambda p: -p.value):
            if (len(self.tasks[priority])):
                return self.tasks[priority][0]