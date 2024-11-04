import json

from pydantic import BaseModel

statuses = {'1': "NotMarked", '2': "Marked", '3': "Finished"}
base_structure = {}
base_structure['NotMarked'] = []
not_marked_counter = 1
base_structure['Marked'] = []
marked_counter = 1
base_structure['Finished'] = []
finished_counter = 1
with open("tasks.json", 'w', encoding='utf-8') as file:
    json.dump(base_structure, file, indent=2, ensure_ascii=False)

class Task(BaseModel):
    task_id: int
    task_description: str
    task_status: str
    task_created: str
    task_updated: str
