from json import load, dump


class PersonalTaskTracker:
    file_structure: dict[str, list] = {
        'NotMarked': [],
        'Marked': [],
        'Finished': []
    }

    def create_file(self, file_name):
        self.file_name = file_name
        self.filename = f"{self.file_name}.json"
        with open(self.filename, 'w', encoding='utf-8') as file:
            dump(self.file_structure, file, indent=3, ensure_ascii=False)

    def open_file(self, file_name):
        self.file_name = file_name
        self.filename = f"{self.file_name}.json"
        with open(self.filename, 'r', encoding='utf-8') as file:
            current_file = load(file)
        print(current_file)