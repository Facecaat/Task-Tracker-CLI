import datetime

class Tasks:
    def __init__(self):
        self.tasks = []
        self.task_id = 0

    @property
    def task(self):
        return self.tasks

    @task.setter
    def task(self, value):
        self.tasks.append(value)

class Task:
    def __init__(self):
        statuses = ["todo", "in-progress", "done"]
        self.id: int = 0
        self.description: str = ""
        self.status: str = statuses[0]
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()
        '''
        id: Уникальный идентификатор для задачи
        description: Краткое описание задачи
        status: Состояние задачи (todo, in-progress, done)
        createdAt: Дата и время создания задачи
        updatedAt: Дата и время последнего обновления задачи
                                                        '''