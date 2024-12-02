from idlelib.iomenu import encoding
from json import load, dump
import datetime


class CommandInteractions:
    task_statuses = {'1': 'NotMarked',
                     '2': 'Marked',
                     '3': 'Finished'}

    # todo нужна ли тут task_structure???
    task_structure = {
        'id': int,
        'description': str,
        'status': str,
        'created': str,
        'updated': str
    }

    def create_task(self, filename, actions):
        self.filename = filename
        self.actions = actions
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        self.additional_task = self.task_structure
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
                file_structure['Finished'].append(item)
                del file_structure['Marked'][index]
                print(f"Task (ID:  {int("".join(self.actions))}) has been successfully removed into Finished")
        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)

    def update_task(self, filename, actions):
        pass