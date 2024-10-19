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

#https://stepik.org/lesson/518492/step/1?unit=510940
#переработать ввод в json-формат и записать его в json-файл
'''
with open('tasks.json', 'w') as file:
    json,dump(command, file)
'''


def running_app():
    while True:
        command = input("task-cli ")
        if command == "add":
            TaskTracker.task = input()
            TaskTracker.task_id += 1
            print(f"Task added successfully (ID: {TaskTracker.task_id})")




