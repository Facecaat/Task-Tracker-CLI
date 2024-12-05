import manager
from json import load, dump



class Application:
    def __init__(self, personal_task_tracker, messages_manager):
        self.personal_task_tracker = personal_task_tracker
        self.messages = messages_manager


    def refresh(self, filename):
        current_id = 1
        with open(filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        for item in file_structure['NotMarked']:
            item['id'] = current_id
            current_id += 1
        current_id = 1
        for item in file_structure['Marked']:
            item['id'] = current_id
            current_id += 1
        current_id = 1
        for item in file_structure['Finished']:
            item['id'] = current_id
            current_id += 1
        with open(filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)
        return filename

    def choose_file(self):
        while True:
            decision = input("Do you want to create/open a tracker?: ")
            if decision == 'exit':
                self.messages.stop_run()
                break
            if decision == "create":
                file_name = input("Write file name you want to create: ")
                self.personal_task_tracker.create_file(file_name)

            elif decision == "open":
                file_name = self.personal_task_tracker.open_file(input("Write file name you want to open: "))
                self.run(file_name)

    def run(self, filename):
        self.current_file = filename
        self.command_interactions = manager.CommandInteractions()
        command, *action = "", ""
        while command != "exit":
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

            self.current_file = self.refresh(self.current_file)
