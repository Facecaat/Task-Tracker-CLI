import classes
import user_inputs_functions

#todo 1. обработка переноса из notmarked в finished
#todo 2. добавить функции вывода определенных списков
#todo 3. переписать на pydentic
#todo 3.1. Вставить каждую таску как класс в код
#todo 3.2. С datetime разобраться как корркетно вставить в инфу о классе
#todo 4. написать тесты
#todo 5. эксепшены
#todo 6. перенести строки обработки команд в файл с функциями
#todo 7. переписать ввод данных в одну строку на каждой функции


def running_app():
    while True:
        command: str = input("task-cli ")
        if command in ["add", "добавить"]:
            task_value: str = input()
            #class_task_dick = classes.Task(classes.not_marked_counter, task_value, classes.statuses['1'], )
            task_dict = {str(classes.not_marked_counter): task_value}
            base_structure = user_inputs_functions.load_json()
            base_structure['NotMarked'].append(task_dict)
            user_inputs_functions.dump_json(base_structure)
            print(f"Task added successfully (ID: {classes.not_marked_counter})")
            classes.not_marked_counter += 1

        if command in ["update", "обновить"]:
            base_structure = user_inputs_functions.load_json()
            id_and_description = input().split(maxsplit=1)



            try:
                task_id = user_inputs_functions.get_id(id_and_description[0])
                description = id_and_description[1] if len(id_and_description) > 1 else ""
                updatable = False
                for item in base_structure['NotMarked']:
                    if str(task_id) in item:
                        item[str(task_id)] = description
                        print(f"Task (ID: {task_id}) now is: {description}")
                        updatable = True
                        break
                if not updatable:
                    print("Error: ID does not exist")
                user_inputs_functions.dump_json(base_structure)

            except TypeError as e:
                print(e)

        if command in ["delete", "удалить"]:
            task_id: str = input()

            try:
                task_id = user_inputs_functions.get_id(task_id)
                base_structure = user_inputs_functions.load_json()
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
                    print("Error: ID does not exist")
                user_inputs_functions.dump_json(base_structure)

            except TypeError as e:
                print(e)


        if command in ["mark-in-progress", "пометить-на-выполнение", "pmark"]:
            task_id: str = input()

            try:
                task_id = user_inputs_functions.get_id(task_id)
                base_structure = user_inputs_functions.load_json()
                for item in base_structure['NotMarked']:
                        if str(task_id) in item:
                            what_to_add = item[str(task_id)]
                            updatable = False
                            base_structure['Marked'].append({str(classes.marked_counter): what_to_add})
                            del item[str(task_id)]
                            print(f"ID {classes.marked_counter}: in 'Marked' now")
                            updatable = True
                            classes.not_marked_counter -= 1
                            classes.marked_counter += 1
                            break

                base_structure['NotMarked'] = [d for d in base_structure['NotMarked'] if d]


                if not updatable:
                    print("Error: ID does not exist")

                user_inputs_functions.dump_json(base_structure)

            except TypeError as e:
                print(e)

        if command in ["mark-done", "поменять-на-окончание", "dmark"]:
            task_id: str = input()

            try:
                task_id = user_inputs_functions.get_id(task_id)
                base_structure = user_inputs_functions.load_json()
                for item in base_structure['Marked']:
                    if str(task_id) in item:
                        what_to_add = item[str(task_id)]
                        updatable = False
                        base_structure['Finished'].append({str(classes.finished_counter): what_to_add})
                        del item[str(task_id)]
                        print(f"ID {classes.finished_counter}: in 'Finished' now")
                        updatable = True
                        classes.marked_counter -= 1
                        classes.finished_counter += 1
                        break
                    else:
                        print("Error: ID does not exist in Marked")

                base_structure['Marked'] = [d for d in base_structure['Marked'] if d]

                if not updatable:
                    print("Error: ID does not exists")

                user_inputs_functions.dump_json(base_structure)

            except TypeError as e:
                print(e)