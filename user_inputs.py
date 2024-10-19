class Tasks:


    def __init__(self, tasks):
        self.tasks = []


    @property
    def task(self):
        return self.tasks

    @task.setter
    def task(self, setting):
        self.tasks.append(setting)


def running_app():
    while True:
        command = input("task-cli ")

running_app()

