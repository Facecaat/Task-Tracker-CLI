from json import load, dump
import datetime


class CommandInteractions:
    task_statuses = {'1': 'NotMarked',
                     '2': 'Marked',
                     '3': 'Finished'}

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
        del file_structure['NotMarked']
