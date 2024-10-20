import json
from dataclasses import dataclass


class Tasks:
    def __init__(self):
        self.tasks = []


    @property
    def task(self):
        return self.tasks


    @task.setter
    def task(self, value):
        self.tasks.append(value)


TaskTracker = Tasks()
statuses = {'1': "NotMarked", '2': "Marked", '3': "Finished"}
base_structure = {}
base_structure['NotMarked'] = []
not_marked_counter = 1
base_structure['Marked'] = []
marked_counter = 1
base_structure['Finished'] = []
finished_counter = 1
with open("tasks.json", 'w') as file:
    json.dump(base_structure, file, indent=2)


@dataclass
class Task:
    task_id: int
    task_description: str
    task_status: str
    task_created: str
    task_updated: str

