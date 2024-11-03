import json
import classes
import datetime

from classes import base_structure


# refreshing lists
def refresh():
    base_structure = load_json()
    if base_structure['NotMarked']:
        classes.not_marked_counter = 1
        for item in base_structure['NotMarked']:
            item['task_id'] = classes.not_marked_counter
            classes.not_marked_counter += 1
    if base_structure['Marked']:
        classes.marked_counter = 1
        for item in base_structure['Marked']:
            item['task_id'] = classes.marked_counter
            classes.marked_counter += 1
    if base_structure['Finished']:
        classes.finished_counter = 1
        for item in base_structure['Finished']:
            item['task_id'] = classes.finished_counter
            classes.finished_counter += 1
    dump_json(base_structure)


# check_ID_is_digit_function
def get_id(id: int):
    if not id.isdigit():
        raise TypeError("Error: ID should be a digit")
    return str(id)


# load_json_function
def load_json():
    with open('tasks.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# dump_json_function
def dump_json(base_structure):
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(base_structure, file, indent=2, ensure_ascii=False)


def add_task(task_value):
    task_data = {
        'task_id': classes.not_marked_counter,
        'task_description': task_value,
        'task_status': classes.statuses['1'],
        'task_created': datetime.datetime.now().strftime('(%d-%m-%Y) %H:%M'),
        'task_updated': datetime.datetime.now().strftime('(%d-%m-%Y) %H:%M')
    }

    class_task_dict = classes.Task(**task_data)
    base_structure = load_json()
    base_structure['NotMarked'].append(class_task_dict.dict())
    dump_json(base_structure)
    print(f"Task added successfully (ID: {classes.not_marked_counter})")
    classes.not_marked_counter += 1


def update_task(id_and_description):
    try:
        base_structure = load_json()
        task_id = get_id(id_and_description[0])
        description = id_and_description[1] if len(id_and_description) > 1 else ""
        updatable = False
        # todo добавь проверку если вводят update lol просто
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
        base_structure = load_json()
        updatable = False
        for index, item in enumerate(base_structure['NotMarked']):
            if item['task_id'] == int(task_id):
                del base_structure['NotMarked'][index]
                print(f"Task deleted successfully (ID: {task_id})")
                updatable = True
                classes.not_marked_counter -= 1
                break

        base_structure['NotMarked'] = [d for d in base_structure['NotMarked'] if d]

        if not updatable:
            print("Error: ID does not exist")
        dump_json(base_structure)

    except TypeError as e:
        print(e)


# todo  *  в конце каждого цикла функцией в run проходить по каждому списку
# todo  *  и переприсваивать id на каждой таске, чтобы все было по-порядку

def pmark_task(task_id):
    updatable = False
    try:
        task_id = get_id(task_id)
        base_structure = load_json()
        for index, item in enumerate(base_structure['NotMarked']):
            if item['task_id'] == int(task_id):
                what_to_add = base_structure['NotMarked'][index]
                what_to_add['task_id'] = classes.marked_counter
                base_structure['Marked'].append(what_to_add)
                del base_structure['NotMarked'][index]
                print(f"ID {task_id}: in 'Marked' now")
                updatable = True
                classes.not_marked_counter -= 1
                classes.marked_counter += 1
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
        base_structure = load_json()
        for index, item in enumerate(base_structure['Marked']):
            if item['task_id'] == int(task_id):
                what_to_add = base_structure['Marked'][index]
                base_structure['Finished'].append(what_to_add)
                del base_structure['Marked'][index]
                print(f"ID {task_id}: in 'Finished' now")
                updatable = True
                classes.marked_counter -= 1
                classes.finished_counter += 1
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
    base_structure = load_json()
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
    base_structure = load_json()
    if base_structure['NotMarked']:
        print("_" * 15)
        print("|Not Marked|")
        for item in base_structure['NotMarked']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    else:
        print("No tasks in Not Marked list")


def task_ml():
    base_structure = load_json()
    if base_structure['Marked']:
        print("_" * 15)
        print("|Marked|")
        for item in base_structure['Marked']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    else:
        print("No tasks in Marked list")

def task_fl():
    base_structure = load_json()
    if base_structure['Finished']:
        print("_" * 15)
        print("|Finished|")
        for item in base_structure['Finished']:
            print(f'{item['task_id']}. {item['task_description']}. Last change was on {item['task_updated']}')
        print("_" * 15)
    else:
        print("No tasks in Finished list")