import manager


# todo *  write tests
# todo *  write exceptions

def run():
   #print("""Welcome to Task-Tracker-CLI app
   #choose what you want to do:
   #1. Create task-list
   #2. Open task-list\n
   #""")
   #user_choise = int(input())
   #match user_choise:
   #    case 1:
   #        input("Name your task-list: ")
   #    case 2:
   #        input("Write task-list name you want to open")

    while True:
        command, *action = input("task-cli ").split()
        if command in ["add", "добавить"]:
            manager.add_task(" ".join(action))

        elif command in ["update", "обновить"]:
            manager.update_task(action)

        elif command in ["delete", "удалить"]:
            task_id = action
            manager.delete_task("".join(task_id))

        elif command in ["mark-in-progress", "пометить-на-выполнение", "pmark"]:
            task_id = action
            manager.pmark_task("".join(task_id))

        elif command in ["mark-done", "поменять-на-окончание", "dmark"]:
            task_id = action
            manager.dmark_task("".join(task_id))

        elif command in ["list", "список"] and len(command) == 1:
            manager.task_list()

        elif command in ["list-to-do", "список-не-выполненных", "nml"]:
            manager.task_nml()

        elif command in ["list-in-progress", "список-на-выполнение", "ml"]:
            manager.task_ml()

        elif command in ["list done", "список-выполненных", "fl"]:
            manager.task_fl()

        else:
            print(f"Error: command '{(command)}' does not exist")

        manager.refresh()
