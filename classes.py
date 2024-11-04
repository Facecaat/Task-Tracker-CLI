from pydantic import BaseModel

class InitializeVariables:
    marked_counter = 1
    not_marked_counter = 1
    finished_counter = 1


class Task(BaseModel):
    task_id: int
    task_description: str
    task_status: str
    task_created: str
    task_updated: str
