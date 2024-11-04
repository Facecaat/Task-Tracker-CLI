import files
from files import load_json, dump_json, FileManager
from classes import InitializeVariables, Task
import application
import datetime


def refresh():
    current_file = application.file_name
    base_structure = load_json(current_file)
    if base_structure['NotMarked']:
        not_marked_counter = 1
        for item in base_structure['NotMarked']:
            item['task_id'] = not_marked_counter
            not_marked_counter += 1
    if base_structure['Marked']:
        marked_counter = 1
        for item in base_structure['Marked']:
            item['task_id'] = marked_counter
            marked_counter += 1
    if base_structure['Finished']:
        finished_counter = 1
        for item in base_structure['Finished']:
            item['task_id'] = finished_counter
            finished_counter += 1
    dump_json(base_structure)


# check_ID_is_digit_function
def get_id(id):
    if not id.isdigit():
        raise TypeError("Error: ID should be a digit")
    return str(id)


def add_task(task_value):
    task_data = {
        'task_id': InitializeVariables.not_marked_counter,
        'task_description': task_value,
        'task_status': files.statuses['1'],
        'task_created': datetime.datetime.now().strftime('(%d-%m-%Y) %H:%M'),
        'task_updated': datetime.datetime.now().strftime('(%d-%m-%Y) %H:%M')
    }

    class_task_dict = Task(**task_data)
    base_structure = load_json(FileManager.get_current_file)
    base_structure['NotMarked'].append(class_task_dict.dict())
    dump_json(base_structure)
    print(f"Task added successfully (ID: {InitializeVariables.not_marked_counter})")
    InitializeVariables.not_marked_counter += 1


def update_task(action):
    try:
        base_structure = load_json(files.filename)
        task_id = get_id(action[0])
        if len(action) == 1:
            print("Error: Expected a new_value")
        else:
            description = " ".join(action[1:])
            updatable = False
            for item in base_structure['NotMarked']:
                if item['task_id'] == int(task_id):
                    item['task_description'] = description
                    item['task_updated'] = datetime.datetime.now().strftime('(%d-%m-%Y) %H:%M')
                    print(f"Task (ID: {task_id}) now is: {description}")
                    updatable = True
                    break
            if not updatable:
                print("Error: ID does not exist")
        dump_json(base_structure)


    except TypeError as e:
        print(e)


def delete_task(task_id):
    try:
        task_id = get_id(task_id)
        base_structure = load_json(files.filename)
        updatable = False
        for index, item in enumerate(base_structure['NotMarked']):
            if item['task_id'] == int(task_id):
                del base_structure['NotMarked'][index]
                print(f"Task deleted successfully (ID: {task_id})")
                updatable = True
                InitializeVariables.not_marked_counter -= 1
                break

        base_structure['NotMarked'] = [d for d in base_structure['NotMarked'] if d]

        if not updatable:
            print("Error: ID does not exist")
        dump_json(base_structure)

    except TypeError as e:
        print(e)


def pmark_task(task_id):
    updatable = False
    try:
        task_id = get_id(task_id)
        base_structure = load_json(files.filename)
        for index, item in enumerate(base_structure['NotMarked']):
            if item['task_id'] == int(task_id):
                what_to_add = base_structure['NotMarked'][index]
                what_to_add['task_status'] = files.statuses['2']
                what_to_add['task_id'] = InitializeVariables.marked_counter
                base_structure['Marked'].append(what_to_add)
                del base_structure['NotMarked'][index]
                print(f"ID {task_id}: in 'Marked' now")
                updatable = True
                InitializeVariables.not_marked_counter -= 1
                InitializeVariables.marked_counter += 1
                break
        for item in base_structure['Marked']:
            if item['task_id'] == int(task_id):
                item['task_updated'] = datetime.datetime.now().strftime('(%d-%m-%Y) %H:%M')
                break

        base_structure['NotMarked'] = [d for d in base_structure['NotMarked'] if d]

        if not updatable:
            print("Error: ID does not exist")

        dump_json(base_structure)

    except TypeError as e:
        print(e)


def dmark_task(task_id):
    updatable = False
    try:
        task_id = get_id(task_id)
        base_structure = load_json(files.filename)
        for index, item in enumerate(base_structure['Marked']):
            if item['task_id'] == int(task_id):
                what_to_add = base_structure['Marked'][index]
                what_to_add['task_status'] = files.statuses['3']
                what_to_add['task_id'] = InitializeVariables.finished_counter
                base_structure['Finished'].append(what_to_add)
                del base_structure['Marked'][index]
                print(f"ID {task_id}: in 'Finished' now")
                updatable = True
                InitializeVariables.marked_counter -= 1
                InitializeVariables.finished_counter += 1
                break
            else:
                print("Error: ID does not exist in Marked")
        for item in base_structure['Finished']:
            if item['task_id'] == int(task_id):
                item['task_updated'] = datetime.datetime.now().strftime('(%d-%m-%Y) %H:%M')
                break

        base_structure['Marked'] = [d for d in base_structure['Marked'] if d]

        if not updatable:
            print("Error: ID does not exists")

        dump_json(base_structure)

    except TypeError as e:
        print(e)


def task_list():
    base_structure = load_json(files.filename)
    if base_structure['NotMarked']:
        print("_" * 15)
        print("|Not Marked|")
        for item in base_structure['NotMarked']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    if base_structure['Marked']:
        print("|Marked|")
        for item in base_structure['Marked']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    if base_structure['Finished']:
        print("|Finished|")
        for item in base_structure['Finished']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)


def task_nml():
    base_structure = load_json(files.filename)
    if base_structure['NotMarked']:
        print("_" * 15)
        print("|Not Marked|")
        for item in base_structure['NotMarked']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    else:
        print("No tasks in Not Marked list")


def task_ml():
    base_structure = load_json(files.filename)
    if base_structure['Marked']:
        print("_" * 15)
        print("|Marked|")
        for item in base_structure['Marked']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    else:
        print("No tasks in Marked list")


def task_fl():
    base_structure = load_json(files.filename)
    if base_structure['Finished']:
        print("_" * 15)
        print("|Finished|")
        for item in base_structure['Finished']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    else:
        print("No tasks in Finished list")
