import json

#Check_ID_is_digit_function
def get_id(id: int):
    if not id.isdigit():
        raise TypeError("Error: ID should be a digit")
    return str(id)

#Load_json_function
def load_json():
    with open('tasks.json', 'r') as file:
        return json.load(file)
