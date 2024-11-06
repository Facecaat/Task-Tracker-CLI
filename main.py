#task-tracker-cli-oop
from application import Application
from files import PersonalTaskTracker

if __name__ == '__main__':
    personal_task_tracker = PersonalTaskTracker()
    application = Application(personal_task_tracker)
    application.choose_file()


