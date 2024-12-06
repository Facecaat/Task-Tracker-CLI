from json import load, dump
from exceptions import UnknownCommand



class Application:
    def __init__(self, personal_task_tracker, command_interactions):
        self.personal_task_tracker = personal_task_tracker
        self.command_interactions = command_interactions


    def refresh(self, filename):
        def update_ids(category):
            for index, value in enumerate(category):
                value['id'] = index + 1

        with open(filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        update_ids(file_structure['NotMarked'])
        update_ids(file_structure['Marked'])
        update_ids(file_structure['Finished'])
        with open(filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)
        return filename

    def choose_file(self):
        while True:
            decision = input("Do you want to create/open/exit a tracker?: ")
            if decision == 'exit':
                print("Program in finished")
                break
            if decision == "create":
                file_name = input("Write file name you want to create: ")
                self.personal_task_tracker.create_file(file_name)
            elif decision == "open":
                file_name = self.personal_task_tracker.open_file(input("Write file name you want to open: "))
                self.run(file_name)


    def run(self, filename):
        self.current_file = filename
        command, *action = "", ""
        while command != "exit":
            try:
                command, *action = input("task-cli ").split()
                if command in ['add', 'добавить']:
                    self.command_interactions.create_task(self.current_file, action)
                elif command in ['del', 'удалить']:
                    self.command_interactions.delete_task(self.current_file, action)
                elif command in ['pmark', 'mark-in-progress', 'пометить-на-выполнение']:
                    self.command_interactions.pmark_task(self.current_file, action)
                elif command in ['dmark', 'mark-done', 'задача-выполнена']:
                    self.command_interactions.dmark_task(self.current_file, action)
                elif command in ['update', 'обновить']:
                    self.command_interactions.update_task(self.current_file, action)
                elif command in ['list', 'lst', 'список']:
                    self.command_interactions.list_of_tasks(self.current_file)
                elif command in ['list-done', 'fl', 'выполненные-задачи']:
                    self.command_interactions.list_of_done(self.current_file)
                elif command in ['list-in-progress', 'ml', 'задачи-на-выполнение']:
                    self.command_interactions.list_of_marked(self.current_file)
                elif command in ['list-todo', 'nml', 'задачи']:
                    self.command_interactions.list_of_not_marked(self.current_file)
                elif command in ['commands']:
                    print(self.command_interactions.commands())
                else:
                    raise UnknownCommand
            except UnknownCommand as e:
                print(e.message)



            self.current_file = self.refresh(self.current_file)
