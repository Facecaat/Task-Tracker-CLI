import json
import classes
import datetime
import user_inputs
from classes import base_structure


#check_ID_is_digit_function
def get_id(id: int):
    if not id.isdigit():
        raise TypeError("Error: ID should be a digit")
    return str(id)


#load_json_function
def load_json():
    with open('tasks.json', 'r') as file:
        return json.load(file)

#dump_json_function
def dump_json(base_structure):
    with open('tasks.json', 'w') as file:
        json.dump(base_structure, file, indent=2)


def add_function(task_value):
    task_data = {
        'task_id': classes.not_marked_counter,
        'task_description': task_value,
        'task_status': classes.statuses['1'],
        'task_created': datetime.datetime.now().isoformat(),
        'task_updated': datetime.datetime.now().isoformat()
    }

    class_task_dict = classes.Task(**task_data)
    print(class_task_dict)
    base_structure = load_json()
    base_structure['NotMarked'].append(class_task_dict.dict())
    dump_json(base_structure)
    print(f"Task added successfully (ID: {classes.not_marked_counter})")
    classes.not_marked_counter += 1


def update_function(id_and_description):
    try:
        base_structure = load_json()
        task_id = get_id(id_and_description[0])
        description = id_and_description[1] if len(id_and_description) > 1 else ""
        updatable = False
        for item in base_structure['NotMarked']:
            item['task_description'] = description
            item['task_updated'] = datetime.datetime.now().isoformat()
            print(f"Task (ID: {task_id}) now is: {description}")
            updatable = True
            break
        if not updatable:
            print("Error: ID does not exist")
        dump_json(base_structure)


    except TypeError as e:
        print(e)
'''
    try:
        base_structure = load_json()
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
            print("Error: ID does not exist")
        dump_json(base_structure)

    except TypeError as e:
        print(e)
'''

def delete_function(task_id):
    try:
        task_id = get_id(task_id)
        base_structure = load_json()
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
        dump_json(base_structure)

    except TypeError as e:
        print(e)


def pmark_function(task_id):
    updatable = False
    try:
        task_id = get_id(task_id)
        base_structure = load_json()
        for item in base_structure['NotMarked']:
            if str(task_id) in item:
                what_to_add = item[str(task_id)]
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

        dump_json(base_structure)

    except TypeError as e:
        print(e)


def dmark_function(task_id):
    updatable = False
    try:
        task_id = get_id(task_id)
        base_structure = load_json()
        for item in base_structure['Marked']:
            if str(task_id) in item:
                what_to_add = item[str(task_id)]
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

        dump_json(base_structure)

    except TypeError as e:
        print(e)
