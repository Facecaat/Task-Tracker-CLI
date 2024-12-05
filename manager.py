
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
        self.filename = filename
        self.actions = actions
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
            check_id = int(self.actions[0])
        for item in file_structure['NotMarked']:
            if item['id'] == int(*self.actions[0]):
                item['description'] = " ".join(self.actions[1:])
                item['updated'] = datetime.datetime.now().strftime("%B %d, %H:%M:%S")
                print(f"Task (ID {int("".join(self.actions[0]))}) has been successfully updated")
        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)

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