#task-tracker-cli-oop
from application import Application
from files import PersonalTaskTracker
from messages import MessageManager

if __name__ == '__main__':
    personal_task_tracker = PersonalTaskTracker()
    messages_manager = MessageManager()
    application = Application(personal_task_tracker, messages_manager)
    application.choose_file()


