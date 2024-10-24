import user_inputs_functions

#todo *  сделать красивый вывод списка дел
#todo *  написать тесты
#todo *  написать эксепшены

def running_app():
    while True:
        command: str = input("task-cli ").split()
        if command[0] in ["add", "добавить"]:
            task_value = command[1]
            user_inputs_functions.add_function(task_value)

        elif command[0] in ["update", "обновить"]:
            id_and_description = command[1], command[2]
            user_inputs_functions.update_function(id_and_description)

        elif command[0] in ["delete", "удалить"]:
            task_id = command[1]
            user_inputs_functions.delete_function(task_id)

        elif command[0] in ["mark-in-progress", "пометить-на-выполнение", "pmark"]:
            task_id = command[1]
            user_inputs_functions.pmark_function(task_id)

        elif command[0] in ["mark-done", "поменять-на-окончание", "dmark"]:
            task_id = command[1]
            user_inputs_functions.dmark_function(task_id)

        elif command[0] in ["list", "список"] and len(command) == 1:
            base_structure = user_inputs_functions.load_json()
            print(base_structure)

        elif command[0] == "nml" or (command[0] in ["list", "список"] and command[1] in ["todo", "не"]):
            base_structure = user_inputs_functions.load_json()
            print(base_structure['NotMarked'])

        elif command[0] == "ml" or (command[0] in ["list", "список"] and command[1] in ["in-progress", "на"]):
            base_structure = user_inputs_functions.load_json()
            print(base_structure['Marked'])

        elif command[0] == "fl" or (command[0] in ["list", "список"] and command[1] in ["done", "выполненных"]):
            base_structure = user_inputs_functions.load_json()
            print(base_structure['Finished'])
        elif command[0] not in ["add", "update", "delete"]:
            print(f"Error: command '{' '.join(command)}' does not exist")