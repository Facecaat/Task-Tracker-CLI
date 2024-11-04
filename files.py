import json
import os


statuses = {'1': "NotMarked", '2': "Marked", '3': "Finished"}

class InitializeBaseStructure:
    base_structure = {}
    base_structure['NotMarked'] = []
    base_structure['Marked'] = []
    base_structure['Finished'] = []

#with open("tasks.json", 'w', encoding='utf-8') as file:
    #json.dump(InitializeBaseStructure.base_structure, file, indent=2, ensure_ascii=False)

class FileManager:
    def __init__(self):
        print("""Welcome to Task-Tracker-CLI app
choose what you want to do:
  1. Create task-list
  2. Open task-list\n""")
        user_choise = int(input("Your input: "))
        match user_choise:
            case 1:
                self.filename = input("Name your task-list: ")
                self.full_filename = f"{self.filename}.json"
                with open(self.full_filename, 'w', encoding='utf-8') as file:
                    json.dump(InitializeBaseStructure.base_structure, file, indent=2, ensure_ascii=False)
                print(f"Task-list {self.full_filename} successfully created")
            case 2:
                self.filename = input("Write task-list name you want to open: ")
                self.full_filename = f"{self.filename}.json"
                self.data = load_json(self.full_filename)
                print(f"Task-list {self.full_filename} successfully opened")

    def get_current_file(self):
        return self.full_filename




def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def dump_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
