
from json import load, dump
import datetime

from exceptions import WrongId


class CommandInteractions:
    task_statuses = {'1': 'NotMarked',
                     '2': 'Marked',
                     '3': 'Finished'}



    def create_task(self, filename, actions):
        self.filename = filename
        self.actions = actions
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        self.additional_task = dict()
        self.additional_task['id'] = 1
        self.additional_task['description'] = " ".join(actions)
        self.additional_task['status'] = self.task_statuses['1']
        self.additional_task['created'] = datetime.datetime.now().strftime("%B %d, %H:%M:%S")
        self.additional_task['updated'] = datetime.datetime.now().strftime("%B %d, %H:%M:%S")
        file_structure['NotMarked'].append(self.additional_task)

        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)
        print(f'"{" ".join(actions)}" added successfully')

    def delete_task(self, filename, actions):
        self.filename = filename
        self.actions = actions
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        for index, item in enumerate(file_structure['NotMarked']):
            if item['id'] == int("".join(self.actions)):
                del file_structure['NotMarked'][index]
                print(f"Task has been deleted {int("".join(self.actions))}")
        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)

    def pmark_task(self, filename, actions):
        self.filename = filename
        self.actions = actions
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        for index, item in enumerate(file_structure['NotMarked']):
            if item['id'] == int("".join(self.actions)):
                item['status'] = self.task_statuses['2']
                item['updated'] = datetime.datetime.now().strftime("%B %d, %H:%M:%S")
                file_structure['Marked'].append(item)
                del file_structure['NotMarked'][index]
                print(f"Task (ID:  {int("".join(self.actions))}) has been successfully removed into Marked")
        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)

    def dmark_task(self, filename, actions):
        self.filename = filename
        self.actions = actions
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        for index, item in enumerate(file_structure['Marked']):
            if item['id'] == int("".join(self.actions)):
                item['status'] = self.task_statuses['3']
                item['updated'] = datetime.datetime.now().strftime("%B %d, %H:%M:%S")
                file_structure['Finished'].append(item)
                del file_structure['Marked'][index]
                print(f"Task (ID:  {int("".join(self.actions))}) has been successfully removed into Finished")
        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)

    def update_task(self, filename, actions):
        try:
            self.filename = filename
            self.actions = actions
            with open(self.filename, 'r', encoding='utf-8') as file:
                file_structure = load(file)
                if not self.actions[0].isdigit():
                    raise WrongId
                else:
                    everything_is_okay = False
                    for item in file_structure['NotMarked']:
                        if item['id'] == int(*self.actions[0]):
                            item['description'] = " ".join(self.actions[1:])
                            item['updated'] = datetime.datetime.now().strftime("%B %d, %H:%M:%S")
                            print(f"Task (ID {int("".join(self.actions[0]))}) has been successfully updated")
                            everything_is_okay = True
                    if not everything_is_okay:
                        raise WrongId
                    with open(self.filename, 'w', encoding='utf-8') as file:
                        dump(file_structure, file, indent=3, ensure_ascii=False)
        except WrongId as e:
            print(e.message)




    def list_of_tasks(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        print("_" * 18)
        print("Not marked tasks:|")
        print("_" * 18)
        for item in file_structure['NotMarked']:
            print(f"{item['id']}: {item['description']}. Last change: {item['updated']}")
        print("_" * 14)
        print("Marked tasks:|")
        print("_" * 14)
        for item in file_structure['Marked']:
            print(f"{item['id']}: {item['description']}. Last change: {item['updated']}")
        print("_" * 16)
        print("Finished tasks:|")
        print("_" * 16)
        for item in file_structure['Finished']:
            print(f"{item['id']}: {item['description']}. Last change: {item['updated']}")

    def list_of_done(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        print("_" * 16)
        print("Finished tasks:|")
        print("_" * 16)
        for item in file_structure['Finished']:
            print(f"{item['id']}: {item['description']}. Last change: {item['updated']}")

    def list_of_marked(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        print("_" * 14)
        print("Marked tasks:|")
        print("_" * 14)
        for item in file_structure['Marked']:
            print(f"{item['id']}: {item['description']}. Last change: {item['updated']}")

    def list_of_not_marked(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        print("_" * 18)
        print("Not marked tasks:|")
        print("_" * 18)
        for item in file_structure['NotMarked']:
            print(f"{item['id']}: {item['description']}. Last change: {item['updated']}")

    def commands(self):
        command_list = ("[add | добавить] [action | действие]\n"
                        "[del | удалить] [id | номер задачи]\n"
                        "[mark-in-progress | пометить-на-выполнение] [id | номер задачи]\n"
                        "[mark-done | задача-выполнена] [id | номер задачи]\n"
                        "[update | обновить] [id | номер задачи] [new action | новое действие]\n"
                        "[list | список] - выводит список всех задач\n"
                        "[list-done | выполненные-задачи] - выводит список выполненных задач\n"
                        "[list-in-progress | задачи-на-выполнение] - выводит список неотмеченных задач\n"
                        "[list-todo | задачи] - выводит список отмеченных задач")
        return command_list