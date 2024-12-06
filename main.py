#task-tracker-cli-oop
from application import Application
from files import PersonalTaskTracker
from manager import CommandInteractions


if __name__ == '__main__':
    personal_task_tracker = PersonalTaskTracker()
    command_interactions = CommandInteractions()
    application = Application(personal_task_tracker, command_interactions)
    application.choose_file()


