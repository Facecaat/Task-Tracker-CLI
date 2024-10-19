class Tasks:

    tasks = []

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




