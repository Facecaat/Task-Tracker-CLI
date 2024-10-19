import datetime
import json


class Tasks:
    def __init__(self):
        self.tasks = []
        self.task_id = 0


    @property
    def task(self):
        return self.tasks


    @task.setter
    def task(self, value):
        self.tasks.append(value)

TaskTracker = Tasks()
base_structure = {}
base_structure['NotMarked'] = []
base_structure['Marked'] = []
base_structure['Finished'] = []
with open("tasks.json", 'w') as file:
    json.dump(base_structure, file, indent=2)

class Task:
    def __init__(self):
        statuses = ["todo", "in-progress", "done"]
        self.id: int = 1
        self.description: str = ""
        self.status: str = statuses[0]
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()
