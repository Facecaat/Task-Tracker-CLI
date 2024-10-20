import json
import user_inputs

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