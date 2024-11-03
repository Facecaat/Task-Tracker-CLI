import manager


# todo *  write tests
# todo *  write exceptions

def run():
    while True:
        command = input("task-cli ").split()
        if command[0] in ["add", "добавить"]:
            manager.add_task(command[1])

        elif command[0] in ["update", "обновить"]:
            id_and_description = command[1], command[2]
            manager.update_task(id_and_description)

        elif command[0] in ["delete", "удалить"]:
            task_id = command[1]
            manager.delete_task(task_id)

        elif command[0] in ["mark-in-progress", "пометить-на-выполнение", "pmark"]:
            task_id = command[1]
            manager.pmark_task(task_id)

        elif command[0] in ["mark-done", "поменять-на-окончание", "dmark"]:
            task_id = command[1]
            manager.dmark_task(task_id)

        elif command[0] in ["list", "список"] and len(command) == 1:
            manager.task_list()

        elif command[0] == "nml" or (command[0] in ["list", "список"] and command[1] in ["todo", "не"]):
            manager.task_nml()

        elif command[0] == "ml" or (command[0] in ["list", "список"] and command[1] in ["in-progress", "на"]):
            manager.task_ml()

        elif command[0] == "fl" or (command[0] in ["list", "список"] and command[1] in ["done", "выполненных"]):
            manager.task_fl()

        elif command[0] not in ["add", "update", "delete"]:
            print(f"Error: command '{' '.join(command)}' does not exist")

        manager.refresh()
