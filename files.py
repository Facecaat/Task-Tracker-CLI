import json
import os

statuses = {'1': "NotMarked", '2': "Marked", '3': "Finished"}

class InitializeBaseStructure:
    base_structure = {}
    base_structure['NotMarked'] = []
    base_structure['Marked'] = []
    base_structure['Finished'] = []



with open("tasks.json", 'w', encoding='utf-8') as file:
    json.dump(InitializeBaseStructure.base_structure, file, indent=2, ensure_ascii=False)

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self._is_file_exists()

    def _is_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump({}, file)


def load_json():
    with open('tasks.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def dump_json(filename):
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(filename, file, indent=2, ensure_ascii=False)
