class Application:
    def __init__(self, personal_task_tracker):
        self.personal_task_tracker = personal_task_tracker

    def choose_file(self):
        while True:
            decision = input("Do you want to create/open a tracker?: ")
            if decision == "create":
                file_name = input("Write file name you want to create: ")
                self.personal_task_tracker.create_file(file_name)


            elif decision == "open":
                file_name = input("Write file name you want to open: ")
                self.run(self.personal_task_tracker.open_file(file_name))




    def run(self, filename):
        command = input("task-cli ")
        while command != "exit":
            command = input("task-cli ")
