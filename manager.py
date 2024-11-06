from json import load, dump


class CommandInteractions:
    def create_task(self, filename, actions):
        self.filename = filename
        self.actions = actions
        with open (self.filename, 'r', encoding='utf-8') as file:
            file_structure = load(file)
        file_structure['NotMarked'].append("".join(actions))
        with open (self.filename, 'w', encoding='utf-8') as file:
            dump(file_structure, file, indent=3, ensure_ascii=False)