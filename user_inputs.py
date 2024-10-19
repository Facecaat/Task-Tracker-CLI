import json

class Tasks:

    tasks = []
    task_id = 0

    @property
    def task(self):
        return self.tasks

    @task.setter
    def task(self, value):
        self.tasks.append(value)

TaskTracker = Tasks()


def running_app():
    while True:
        command = input("task-cli ")
        if command == "add":
            TaskTracker.task = input()
            TaskTracker.task_id += 1
            print(f"Task added successfully (ID: {TaskTracker.task_id})")




