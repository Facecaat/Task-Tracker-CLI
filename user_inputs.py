import json

def running_app():
    while True:
        command: str = input("task-cli ")
        if command in ["add", "добавить"]:
            TaskTracker.task_id += 1
            task_value: str = input()
            task_dict = {str(TaskTracker.task_id): task_value}

            with open('tasks.json', 'r') as file:
                base_structure = json.load(file)

            base_structure['NotMarked'].append(task_dict)

            with open('tasks.json', 'w') as file:
                json.dump(base_structure, file, indent=2)

            print(f"Task added successfully (ID: {TaskTracker.task_id})")

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
