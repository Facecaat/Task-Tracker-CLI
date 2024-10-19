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
with open("tasks.json", 'w') as file:
    json.dump(base_structure, file, indent=2)


def running_app():
    while True:
        command = input("task-cli ")
        if command in ["add", "добавить"]:
            TaskTracker.task_id += 1
            task_value = input()
            task_dict = {TaskTracker.task_id: task_value}

            with open('tasks.json', 'r') as file:
                base_structure = json.load(file)

            base_structure['NotMarked'].append(task_dict)

            with open('tasks.json', 'w') as file:
                json.dump(base_structure, file, indent=2)

            print(f"Task added successfully (ID: {TaskTracker.task_id})")

        if command in ["update", "обновить"]:
            with open("tasks.json") as file:
                tasks_data_json = json.load(file)
                print(tasks_data_json)






