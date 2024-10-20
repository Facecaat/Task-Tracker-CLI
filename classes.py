import datetime
import json
from pydantic import BaseModel


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
statuses = ["NotMarked", "Marked", "Finished"]
base_structure = {}
base_structure['NotMarked'] = []
not_marked_counter = 1
base_structure['Marked'] = []
marked_counter = 1
base_structure['Finished'] = []
finished_counter = 1
with open("tasks.json", 'w') as file:
    json.dump(base_structure, file, indent=2)


class Task(BaseModel):
    Task_id: int
    Task_description: str
    Task_status: str
    Task_created: datetime.datetime
    Task_updated: datetime.datetime

