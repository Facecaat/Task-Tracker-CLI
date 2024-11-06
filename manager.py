from json import load, dump


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
        with open (self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        file_structure['NotMarked'].append("".join(actions))
        with open (self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)

    #todo добавить модуль datetime и вывод времени ну и собственно
    #todo оформить каждую таску по task_structure