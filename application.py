import manager


class Application:
    def __init__(self, personal_task_tracker):
        self.personal_task_tracker = personal_task_tracker

    def refresh(self):
        pass

    def choose_file(self):
        while True:
            decision = input("Do you want to create/open a tracker?: ")
            if decision == 'exit':
                print("Program in finished")
                break
            if decision == "create":
                file_name = input("Write file name you want to create: ")
                self.personal_task_tracker.create_file(file_name)

            elif decision == "open":
                file_name = input("Write file name you want to open: ")
                self.run(f"{file_name}.json")

    def run(self, filename):
        self.current_file = filename
        self.command_interactions = manager.CommandInteractions()
        print(self.current_file)
        command, *action = "", ""
        while command != "exit":
            command, *action = input("task-cli ").split()
            print(command, *action)
            if command in ['add', 'добавить']:
                print(action)
                self.command_interactions.create_task(self.current_file, action)

            refresh()

