import classes
import json

def running_app():
    while True:
        command: str = input("task-cli ")
        if command in ["add", "добавить"]:
            task_value: str = input()
            task_dict = {str(classes.not_marked_counter): task_value}
            with open('tasks.json', 'r') as file:
                base_structure = json.load(file)
            base_structure['NotMarked'].append(task_dict)
            print(base_structure)
            with open('tasks.json', 'w') as file:
                json.dump(base_structure, file, indent=2)
            print(f"Task added successfully (ID: {classes.not_marked_counter})")
            classes.not_marked_counter += 1

        if command in ["update", "обновить"]:
            with open('tasks.json', 'r') as file:
                base_structure = json.load(file)
            id_and_description = input().split(maxsplit=1)

            def get_id(id: int):
                if not id.isdigit():
                    raise TypeError("Error: ID should be a digit")
                return int(id)

            try:
                task_id = get_id(id_and_description[0])
                description = id_and_description[1] if len(id_and_description) > 1 else ""
                updatable = False
                for item in base_structure['NotMarked']:
                    if str(task_id) in item:
                        item[str(task_id)] = description
                        print(f"Task (ID: {task_id}) now is: {description}")
                        updatable = True
                        break
                if not updatable:
                    print("Error: ID is not exist")
                with open('tasks.json', 'w') as file:
                    json.dump(base_structure, file, indent=2)

            except TypeError as e:
                print(e)

        if command in ["delete", "удалить"]:
            task_id: str = input()

            def get_id(id: int):
                if not id.isdigit():
                    raise TypeError("Error: ID should be a digit")
                return int(id)


            with open('tasks.json', 'r') as file:
                base_structure = json.load(file)

            try:
                updatable = False
                for item in base_structure['NotMarked']:
                    if str(task_id) in item:
                        del item[str(task_id)]
                        print(f"Task deleted successfully (ID: {task_id})")
                        updatable = True
                        classes.not_marked_counter -= 1
                        break

                base_structure['NotMarked'] = [d for d in base_structure['NotMarked'] if d]

                if not updatable:
                    print("Error: ID is not exist")
                with open('tasks.json', 'w') as file:
                    json.dump(base_structure, file, indent=2)

            except TypeError as e:
                print(e)


        if command in ["mark-in-progress", "пометить-на-выполнение", "pmark"]:
            task_id: str = input()
            def get_id(id: int):
                if not id.isdigit():
                    raise TypeError("Error: ID should be a digit")
                return int(id)
            try:
                task_id = get_id(task_id)
                with open('tasks.json', 'r') as file:
                    base_structure = json.load(file)
                    for item in base_structure['NotMarked']:
                        if str(task_id) in item:
                            what_to_add = item[str(task_id)]
                            updatable = False
                            base_structure['Marked'].append({str(classes.marked_counter): what_to_add})
                            del item[str(task_id)]
                            print(f"ID {item}: in 'Marked' now")
                            updatable = True
                            classes.not_marked_counter -= 1
                            classes.marked_counter += 1
                            break

                base_structure['NotMarked'] = [d for d in base_structure['NotMarked'] if d]


                if not updatable:
                    print("Error: ID is not exist")

                with open('tasks.json', 'w') as file:
                    json.dump(base_structure, file, indent=2)

            except TypeError as e:
                print(e)
