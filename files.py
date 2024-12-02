from json import load, dump
from exceptions import FileDoesNotExist
import os


class PersonalTaskTracker:
    file_structure: dict[str, list] = {
        'NotMarked': [],
        'Marked': [],
        'Finished': []
    }

    def __init__(self, filename=None):
        self.filename = filename

    def create_file(self, filename):
        self.filename = f"{filename}.json"
        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(self.file_structure, file, indent=3, ensure_ascii=False)

    def open_file(self, filename):
        while True:
            try:
                self.filename = f"{filename}.json"
                if os.path.exists(self.filename):
                    with open(self.filename, 'r', encoding='utf-8') as file:
                        print(f'{self.filename.strip(".json")} successfully opened!')
                        return self.filename
                else:
                    raise FileDoesNotExist
            except FileDoesNotExist as e:
                print(e.message)
                filename = (input("Write file name you want to open: "))


