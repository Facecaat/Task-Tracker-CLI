import datetime
import json


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
base_structure = {}
base_structure['NotMarked'] = []
not_marked_counter = 1
base_structure['Marked'] = []
marked_counter = 1
base_structure['Finished'] = []
finished_counter = 1
with open("tasks.json", 'w') as file:
    json.dump(base_structure, file, indent=2)

'''
class Task:
    def __init__(self, description):
        statuses = ["todo", "in-progress", "done"]
        self.id: int
        self.description: description
        self.status: str = statuses[0]
        self.createdAt = datetime.datetime.now()
        self.updatedAt = datetime.datetime.now()
'''